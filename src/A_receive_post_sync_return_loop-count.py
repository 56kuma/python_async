# 🟠C_6とセットで起動

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import time

class MySyncHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        loop_count = data.get('loop_count', [''])[0]

        # response_text = "Received loop_count: {}".format(loop_count)
        response_text = loop_count

        # 明示的にsleep
        print(loop_count)
        if int(loop_count) % 10 == 0:
            print("🟠true")
            time.sleep(1)

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))

PORT = 8080

Handler = MySyncHandler
httpd = HTTPServer(("", PORT), Handler)

print("Serving at port {}".format(PORT))

httpd.serve_forever()
