import statistics


def calculate_metrics(response_times):
    return {
        "average_ms": round(statistics.mean(response_times), 2),
        "p95_ms": round(statistics.quantiles(response_times, n=20)[18], 2),
        "max_ms": round(max(response_times), 2)
    }
