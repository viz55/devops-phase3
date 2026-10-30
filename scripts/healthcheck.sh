#!/bin/bash
set -euo pipefail

health_url="${HEALTH_URL:-http://localhost:8080/health}"
max_attempts=3

for attempt in $(seq 1 "$max_attempts"); do
  if curl -sf "$health_url" > /dev/null; then
    echo "healthy after attempt ${attempt}"
    exit 0
  fi
  sleep 2
done

echo "health check failed after ${max_attempts} attempts" >&2
exit 1
