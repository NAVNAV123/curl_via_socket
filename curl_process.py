import socket

class HTTPRequest(object):

    def __init__(self, host):
        self.headers = {}
        self.method = {}
        self.host = host
        self.socket = socket.socket()
        self.socket.connect((self.host, 443))

    def send(self): #TODO: check how i can put in the headers also
        self.socket.send()#HOW can i combine all those headers into one piece and send them?!

x = HTTPRequest("www.google.com")
x.headers["Content-type"] = "application/json"
x.method["message"] = "GET"
# x.send() #TODO: refer this to send function

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
