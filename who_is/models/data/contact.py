from who_is.models.data.address import Address
from who_is.models.generics.whois_data_object import WhoisDataObject, WhoisDataField


class ContactWrapper(WhoisDataObject):
    _types: list = []
    _contacts: dict = {}
    _search_types: dict = {
        "admin": ["admin", "administrative"],
        "tech": ["tech", "technological"],
        "registrant": ["registrant"]
    }

    def __init__(self, whois_dict: dict):
        super().__init__(whois_dict)
        sub_dicts = {
            k: {} for k in self._search_types
        }
        for key, value in whois_dict.items():
            first_key = key.split("_")[0]
            for contact_type, search_keys in self._search_types.items():
                if first_key in search_keys:
                    sub_dicts[contact_type][key] = value

        for contact_type, sub_dict in sub_dicts.items():
            self._contacts[contact_type] = Contact(whois_dict=sub_dict)

    def json(self) -> dict:
        return {
            k: v.json()
            for k, v in self._contacts.items()
        }


class Contact(WhoisDataObject):
    name: str
    organization: str
    address: Address
    email: str
    phone: str
    fax: str
    registry_id: str

    _fields = {
        'name': WhoisDataField(matching_keys=['name']),
        'organization': WhoisDataField(matching_keys=['organization', 'organisation']),
        'address': WhoisDataField(matching_keys=[], data_type=Address),
        'email': WhoisDataField(matching_keys=["mail"]),
        'phone': WhoisDataField(matching_keys=['phone']),
        'fax': WhoisDataField(matching_keys=["fax"], validator="email"),
        'registry_id': WhoisDataField(matching_keys=["registry_id", "id"])
       }
