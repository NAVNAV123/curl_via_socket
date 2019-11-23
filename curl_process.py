import socket

class HTTPRequest(object):

    def __init__(self, url):
        self.headers = {}
        self.method = {}
        self.url = url
    # def send(self):                  #TODO: check how i can put in the headers also
    #     self.socket = socket.socket()
    #     self.connection, _ = self.socket.create_connection((self.url, 443))
    #     self.streaming()
    
x = HTTPRequest("https://google.com/") #TODO: I need to receive client input include the headers
x.headers["Content-type"] = "application/json"
x.method["message"] = "GET/auth HTTP/1.1\r\n"
# x.send() #TODO: refer this to send function

s = socket.socket()
s.bind(('', 8080))
s.listen(5)
client, adress = s.accept()

print("Incoming:", adress)
print(client.recv(1024))
print

client.send(x.method + '\r\n')
client.send(x.headers + "\r\n\r\n")
client.send('<html><body><h1>Hello World</body></html>')
client.close()

print("Answering ...")
print("Finished.")

print(s.recv(1024))
s.close()


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(host, 443)
# s.sendall(x.method + x.headers + "\r\n")
