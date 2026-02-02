import json
from core.api_client import call_api
from core.metrics import calculate_metrics
from core.validator import (
    validate_max_response_time,
    validate_p95,
    validate_error_rate,
)
from config.config import (
    TOTAL_RUNS,
    WARM_UP_RUNS,
    MAX_SINGLE_RESPONSE_MS,
    P95_THRESHOLD_MS,
    ERROR_RATE_THRESHOLD,
)


def test_api_performance():
    response_times = []
    errors = 0

    # -------- Warm-up (ignored) --------
    for _ in range(WARM_UP_RUNS):
        call_api()

    # -------- Measured runs --------
    for _ in range(TOTAL_RUNS):
        response, elapsed_ms = call_api()

        validate_max_response_time(elapsed_ms, MAX_SINGLE_RESPONSE_MS)

        response_times.append(elapsed_ms)
        if response.status_code != 200:
            errors += 1

    metrics = calculate_metrics(response_times)

    report = {
        "runs": TOTAL_RUNS,
        "metrics": metrics,
        "error_rate_percent": round((errors / TOTAL_RUNS) * 100, 2),
    }

    print("\n--- Performance Report ---")
    print(json.dumps(report, indent=2))

    validate_p95(metrics["p95_ms"], P95_THRESHOLD_MS)
    validate_error_rate(errors, TOTAL_RUNS, ERROR_RATE_THRESHOLD)
