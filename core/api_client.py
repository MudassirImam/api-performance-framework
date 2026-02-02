import time
import requests
from config.config import BASE_URL, ENDPOINT, TIMEOUT_SECONDS


def call_api():
    start = time.perf_counter()
    response = requests.get(
        BASE_URL + ENDPOINT,
        timeout=TIMEOUT_SECONDS
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    return response, elapsed_ms
