from who_is.models.data.contact import ContactWrapper
from who_is.models.data.dates import Dates
from who_is.models.data.general import General
from who_is.models.data.registrar import Registrar


class WhoisResponse:
    registrar: Registrar
    dates: Dates
    contact: ContactWrapper
    general: General

    def __init__(self, whois_dict: dict):
        self.registrar = Registrar(whois_dict=whois_dict)
        self.dates = Dates(whois_dict=whois_dict)
        self.contact = ContactWrapper(whois_dict=whois_dict)
        self.general = General(whois_dict=whois_dict)

    def json(self):
        return {
            **self.general.json(),
            'registrar': self.registrar.json(),
            'dates': self.dates.json(),
            'contact': self.contact.json(),
        }
