import socket

from who_is.models.whois_raw_response import WhoisRawResponse


class WhoisSocket:
    sock: socket.socket

    def __init__(self, server: str):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server, 43))

    def _receive(self):
        data = []
        while True:
            chunk = self.sock.recv(1024)
            if chunk == b"":
                break
            else:
                data.append(chunk.decode())

        return "".join(data)

    def query(self, domain: str) -> WhoisRawResponse:
        query_data = domain + "\r\n"
        x = self.sock.send(query_data.encode())
        data = self._receive()
        return WhoisRawResponse(data)
