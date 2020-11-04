import socket
from urllib.parse import urlparse

METHODS = {"GET", "POST", "PUT", "UPDATE", "DELETE"}

class HTTPRequest(object):

    def __init__(self, method, url, headers=None):
        self.url = url
        self.url_parts = urlparse(url)
        self.method = method
        if method not in METHODS:
            raise ValueError("worng method")
        self.headers = {
            "Host": self.url_parts.netloc,
            "User-Agent": "nevehttp/90.0.4",
            "Accept": "*/*"
        }
        if headers is not None:
            self.headers.update(headers)

    def _get_payload(self):
        payload = "%s %s HTTP/1.1\r\n" % (self.method, self.url_parts.path)
        for header in self.headers:
            payload = payload + "%s: %s\r\n " % (header, self.headers[header])
        payload += "\r\n"
        return payload.encode()

    def _read_scokets(self, s):  # TCP: read the socket until the end of the file.
        response = b""
        while True:
            buffer = s.recv(1024)
            if not buffer:
                break
            response += buffer
        return response

    def send(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        http_payload = self._get_payload()
        try:
            print("Connecting to %s" % self.url_parts.netloc)
            s.connect((self.url_parts.netloc, 80))
            print("connected")

            print("sending payload")
            print(http_payload)
            s.sendall(http_payload)
            print("payload sent")

            print("Reading payload")
            print(self._read_scokets(s))

        except socket.error as e:
            e.close()


packet_req = HTTPRequest("GET", "https://www.google.com", headers={"Content-type": "Application/JSON"})
packet_req.send()
