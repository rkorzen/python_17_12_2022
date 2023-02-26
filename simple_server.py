from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(level=logging.INFO)


class SimpleServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        logging.info(
            f"""GET request,
    Path: {self.path}
    Headers: {self.headers}    
        """
        )

        self._set_response()
        self.wfile.write(f"GET request for path {self.path}".encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        logging.info(
            f"""
POST request
Path: {self.path}
Headers: {self.headers}
Body: {post_data.decode()}        
        
        """
        )
        self._set_response()
        self.wfile.write(f"POST request for {self.path}".encode())


def run(server_class=HTTPServer, handler_class=SimpleServer, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd ...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:  # ctrl+c
        httpd.server_close()

    logging.info("Stopping httpd ... \n")


if __name__ == "__main__":
    run()
