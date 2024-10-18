import json

from who_is import whois

googlecom = whois("google.com")
print(json.dumps(googlecom.json(), indent=4))