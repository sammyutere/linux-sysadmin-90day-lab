> **Rocky Linux Note**
>
> Rocky/RHEL systems run `firewalld` by default.
> For node_exporter metrics to be reachable from the host, TCP port 9100 must be explicitly allowed:
>
> ```bash
> sudo firewall-cmd --add-port=9100/tcp --permanent
> sudo firewall-cmd --reload
> ```
>
> Without this step, metrics requests will fail with `connection refused`
> even if the service is running and listening locally.

