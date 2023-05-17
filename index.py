from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'https://cornrepublic.com/zz/ch/measpx.php?trinity=ok')
        self.end_headers()

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8080), MyHandler)
    print('Loading')
    httpd.serve_forever()
