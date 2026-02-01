#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime, os

LOG_PATH = os.environ.get("WEBHOOK_LOG", "monitoring/webhook/notifications.log")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="replace")
        ts = datetime.datetime.utcnow().isoformat() + "Z"
        entry = f"\n---\n{ts}\n{self.client_address[0]} {self.path}\n{body}\n"
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(entry)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok\n")

    def log_message(self, format, *args):
        # Silence default request logging to keep output clean
        return

if __name__ == "__main__":
    port = int(os.environ.get("WEBHOOK_PORT", "9099"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Webhook receiver listening on :{port}, logging to {LOG_PATH}")
    server.serve_forever()
