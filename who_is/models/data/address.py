from who_is.models.generics.whois_data_object import WhoisDataObject, WhoisDataField


class Address(WhoisDataObject):
    street: str
    city: str
    postal_code: str
    state: str
    country: str

    _fields = {
        'street': WhoisDataField(matching_keys=["street"]),
        'city': WhoisDataField(matching_keys=["city"]),
        'postal_code': WhoisDataField(matching_keys=["postal_code", "postal"]),
        'state': WhoisDataField(matching_keys=["state"]),
        'country': WhoisDataField(matching_keys=["country"]),
    }

    def __init__(self, whois_dict: dict):
        super().__init__(whois_dict)

        address_keys = [key for key in whois_dict.keys() if "address" in key]
        # TODO: implement geocoding


