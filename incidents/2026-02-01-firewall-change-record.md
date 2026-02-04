# Change Record — Allow TCP/9100 on infra-rocky

## Change Description
Allowed inbound TCP/9100 on infra-rocky to permit Prometheus access to node_exporter.

## Reason for Change
Monitoring visibility was blocked by default firewall rules.

## Change Details
- Command: `firewall-cmd --add-port=9100/tcp --permanent`
- Reloaded firewall rules

## Risk Assessment
Low risk. Change limited to monitoring port.

## Validation
- Metrics endpoint reachable from host
- Prometheus target marked UP
- Alert resolved

## Rollback Plan
Remove firewall rule and reload firewalld if required.

## Approval
Lab environment — self-approved

