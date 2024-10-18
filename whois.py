from who_is.models.whois_raw_response import WhoisRawResponse
from who_is.net.whois_socket import WhoisSocket


class Whois:
    _response: WhoisRawResponse
    _wsocket: WhoisSocket

    def __init__(self, domain: str):
        self._wsocket = WhoisSocket(server="whois.psi-usa.info")
        self._response = self._wsocket.query(domain)

