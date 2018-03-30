from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_POST(self):
        clen = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(clen))
        self._set_headers()
        self.wfile.write("{" + '"validationResponse": "' +  data[0]['data']['validationCode'] + '"}')


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    print('Running...')
    server.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()