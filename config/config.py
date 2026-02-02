BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"

TOTAL_RUNS = 10
WARM_UP_RUNS = 2

MAX_SINGLE_RESPONSE_MS = 1500     # Safety guardrail
P95_THRESHOLD_MS = 800             # SLA
ERROR_RATE_THRESHOLD = 0.05

TIMEOUT_SECONDS = 5
