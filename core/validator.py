def validate_max_response_time(elapsed_ms, max_allowed):
    assert elapsed_ms <= max_allowed, (
        f"Extreme latency detected: {elapsed_ms:.2f} ms "
        f"(max allowed {max_allowed} ms)"
    )


def validate_p95(p95_value, threshold):
    assert p95_value <= threshold, (
        f"P95 latency {p95_value:.2f} ms exceeded SLA "
        f"{threshold} ms"
    )


def validate_error_rate(errors, total_runs, threshold):
    error_rate = errors / total_runs
    assert error_rate <= threshold, (
        f"Error rate {error_rate * 100:.2f}% exceeded "
        f"{threshold * 100:.2f}%"
    )
