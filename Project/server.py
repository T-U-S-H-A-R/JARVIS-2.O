import http.server
import socketserver
import subprocess
import json
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # TIME button
        if self.path == "/time":
            result = subprocess.run(["python", "time.py"], capture_output=True, text=True)
            output = result.stdout + result.stderr
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(output.encode())
        else:
            super().do_GET()

    def do_POST(self):
        output = ""
        try:
            if self.path == "/runScript":
                result = subprocess.run(["python", "script.py"], capture_output=True, text=True)
                output = result.stdout + result.stderr

            elif self.path == "/runJarvis":
                result = subprocess.run(["python", "JARVIS_2.O.py"], capture_output=True, text=True)
                output = result.stdout + result.stderr

            elif self.path == "/runGoogle":
                result = subprocess.run(["python", "google.py"], capture_output=True, text=True)
                output = result.stdout + result.stderr

            # ✅ New route for introduction.py
            elif self.path == "/runIntro":
                result = subprocess.run(["python", "introduction.py"], capture_output=True, text=True)
                output = result.stdout + result.stderr

            else:
                self.send_error(404)
                return

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"output": output}).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"output": str(e)}).encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()