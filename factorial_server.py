from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import math


def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return math.factorial(n)


class FactorialHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/factorial":
            self._send_json(404, {"error": "not found"})
            return

        query = parse_qs(parsed.query)
        values = query.get("n")
        if not values:
            self._send_json(400, {"error": "missing query parameter n"})
            return

        raw_n = values[0]
        try:
            n = int(raw_n)
        except ValueError:
            self._send_json(400, {"error": "n must be an integer"})
            return

        if n < 0:
            self._send_json(400, {"error": "n must be a non-negative integer"})
            return

        value = calculate_factorial(n)
        self._send_json(200, {"n": str(n), "factorial": str(value)})


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), FactorialHandler)
    print("Factorial server listening on http://0.0.0.0:8000")
    server.serve_forever()
