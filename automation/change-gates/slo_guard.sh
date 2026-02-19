#!/bin/bash
set -euo pipefail

THRESHOLD=0.995
RESULT=$(curl -sSfG "http://localhost:9090/api/v1/query" \
  --data-urlencode 'query=avg_over_time(up{job="node"}[30m])' \
  | jq -r '.data.result[0].value[1]')

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

if (( $(echo "$RESULT < $THRESHOLD" | bc -l) )); then
  echo "$TS - BLOCKED: Availability $RESULT below threshold $THRESHOLD"
  exit 1
else
  echo "$TS - APPROVED: Availability $RESULT meets threshold"
  exit 0
fi

