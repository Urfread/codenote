from http.server import BaseHTTPRequestHandler,HTTPServer
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
def run(server_class=HTTPServer,handler_class=SimpleHTTPRequestHandler):
    server_address = ('',8000) # 服务器地址和端口
    httpd = server_class(server_address,handler_class) # 创建服务器对象
    print('Server running...')
    httpd.serve_forever() # 启动服务器
if __name__ == '__main__':
    run()