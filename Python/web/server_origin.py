from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # 获取请求的路径
        path = self.path

        # 根据路径返回不同的响应
        if path == '/':
            self.handle_home()
        elif path == '/about':
            self.handle_about()
        else:
            self.handle_404()

    def handle_home(self):
        # 首页的响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.add_cors_header()
        self.end_headers()
        message = '{"message": "Welcome to the home page."}'
        self.wfile.write(message.encode())

    def handle_about(self):
        # 关于页的响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.add_cors_header()
        self.end_headers()
        message = '{"message": "This is the about page."}'
        self.wfile.write(message.encode())

    def handle_404(self):
        # 404 Not Found 响应
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = '{"error": "404 Not Found"}   '
        self.wfile.write(message.encode())
    def add_cors_header(self):
        # 允许所有域名访问资源（在生产环境中，应该指定具体的域名）
        self.send_header('Access-Control-Allow-Origin', '*')
        # 如果需要支持cookies，还需要添加以下头部
        self.send_header('Access-Control-Allow-Credentials', 'true')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server starting on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()