import http.server
import socketserver
import os
from jinja2 import Environment, FileSystemLoader

PORT = 8000

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request: Path={self.path}, Headers={self.headers}")

        if self.path == '/resume':
            template = env.get_template("resume_template.html")
            resume_data = {
                "name": "Venu Gopal Myneni",
                "email": "m@example.com",
                "phone": "+1234567890",
                "experience": [
                    {"position": "Software Engineer", "company": "TechCorp", "years": "2018-2023"},
                    {"position": "Web Developer", "company": "WebWorks", "years": "2015-2018"},
                ],
                "skills": ["Python", "Django", "Flask", "Jinja2"]
            }
            content = template.render(resume_data)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
