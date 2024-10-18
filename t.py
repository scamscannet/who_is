import json

from who_is import whois

googlecom = whois("interbloc.org")
print(json.dumps(googlecom.json(), indent=4))