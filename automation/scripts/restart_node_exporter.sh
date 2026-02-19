#!/bin/bash
set -euo pipefail

LOGFILE="$(pwd)/automation/logs/node_exporter_auto_restart.log"
TS="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

echo "$TS - Webhook triggered: attempting remote restart on infra-rocky" | tee -a "$LOGFILE"

# Run the restart on the VM (where systemctl exists)
vagrant ssh infra-rocky -c "sudo systemctl restart node_exporter"

# Verify service status on the VM
if vagrant ssh infra-rocky -c "systemctl is-active --quiet node_exporter"; then
  echo "$TS - SUCCESS: node_exporter is active on infra-rocky" | tee -a "$LOGFILE"
else
  echo "$TS - FAIL: node_exporter is NOT active on infra-rocky" | tee -a "$LOGFILE"
  exit 1
fi

