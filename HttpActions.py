import socket

class HTTPRequest(object):

    def __init__(self, url):
        self.headers = {}
        self.method = {}
        self.url = url

x = HTTPRequest("https://google.com/") #TODO: I need to receive client input include the headers
x.headers["Content-type"] = "application/json"
x.method["message"] = "GET/auth HTTP/1.1\r\n"
host = socket.gethostbyname(x.url)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host, 443)
s.sendall(x.method + x.headers + "\r\n")

print(s.recv(1024))