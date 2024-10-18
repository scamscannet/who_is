from who_is.models.data.address import Address
from who_is.models.generics.whois_data_object import WhoisDataObject, WhoisDataField


class Registrar(WhoisDataObject):
    name: str
    iana_id: str
    address: Address
    url: str
    abuse_email: str
    abuse_phone: str
    whois: str

    _fields = {'iana_id': WhoisDataField(matching_keys=['iana_id']),
               'name': WhoisDataField(matching_keys=['registrar']),
               'address': WhoisDataField(matching_keys=[], data_type=Address),
               'url': WhoisDataField(matching_keys=["registrar_url"]),
               'abuse_phone': WhoisDataField(matching_keys=["abuse_phone", "abuse_contact_phone"]),
               'abuse_email': WhoisDataField(matching_keys=["abuse_email", "abuse_contact_email"]),
               'whois': WhoisDataField(matching_keys=["registrar_whois"])
               }
