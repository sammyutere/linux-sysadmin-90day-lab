from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess
import os
from datetime import datetime

EVIDENCE_PATH = "lab/evidence/last_alertmanager_payload.json"
LOG_PATH = "automation/logs/webhook_receiver.log"

os.makedirs("lab/evidence", exist_ok=True)
os.makedirs("automation/logs", exist_ok=True)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)

        # Write raw payload for evidence every time
        with open(EVIDENCE_PATH, "wb") as f:
            f.write(body)

        ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(LOG_PATH, "a") as f:
            f.write(f"{ts} - Received POST {self.path}, wrote {EVIDENCE_PATH}\n")

        # Attempt to parse JSON and act on NodeExporterDown
        try:
            data = json.loads(body.decode("utf-8"))
        except Exception as e:
            with open(LOG_PATH, "a") as f:
                f.write(f"{ts} - ERROR parsing JSON: {e}\n")
            self.send_response(200)
            self.end_headers()
            return

        restarted = False
        for alert in data.get("alerts", []):
            name = alert.get("labels", {}).get("alertname")
            if name == "NodeExporterDown":
                subprocess.run(["/bin/bash", "automation/scripts/restart_node_exporter.sh"], check=False)
                restarted = True

        with open(LOG_PATH, "a") as f:
            f.write(f"{ts} - Processed alerts. Restart attempted: {restarted}\n")

        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # reduce console noise
        return

if __name__ == "__main__":
    print("Webhook receiver listening on 0.0.0.0:8080")
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

