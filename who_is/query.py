from who_is.models.whois_response import WhoisResponse
from who_is.net.whois_socket import WhoisSocket
from who_is.utils.extractors.next_whois import next_whois_server


def whois(domain: str, whois_server: str = "whois.iana.org", recursive: bool = True) -> WhoisResponse:
    if recursive:
        return recursive_whois(domain, whois_server)
    else:
        return single_whois(domain, whois_server)


def recursive_whois(domain: str, whois_server: str = "whois.iana.org", checked_servers: list = []) -> WhoisResponse:
    s = WhoisSocket(whois_server)
    r = s.query(domain)
    next_server = next_whois_server(whois_dict=r.json(), exclude=checked_servers)

    if next_server:
        checked_servers.append(next_server)
        return recursive_whois(domain=domain, whois_server=next_server, checked_servers=checked_servers)

    else:
        return r.format()


def single_whois(domain: str, whois_server: str) -> WhoisResponse:
    s = WhoisSocket(whois_server)
    r = s.query(domain)
    return r.format()
