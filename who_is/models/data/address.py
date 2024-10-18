from who_is.net.nominatim import query_unformatted_address

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
        'country_code': WhoisDataField(matching_keys=["country_code"]),
    }

    def __init__(self, whois_dict: dict):
        super().__init__(whois_dict)

        address_keys = [key for key in whois_dict.keys() if "address" in key]

        address_components = []
        for key in address_keys:
            value = whois_dict[key]

            if isinstance(value, list):
                address_components.append(*value)
            else:
                address_components.append(value)

        parsed_address_components = [
            self.street,
            self.city if self.city else "" + (" " + self.postal_code) if self.postal_code else "",
            self.state,
            self.country
        ]

        parsed_address_components = [x for x in parsed_address_components if x is not None and len(x) > 0]

        picked_address_components = address_components \
            if len(address_components) > len(parsed_address_components) else \
            parsed_address_components

        addres_string = " , ".join(picked_address_components)

        formatted_address = query_unformatted_address(addres_string)

        for k, v in formatted_address.items():
            if v is not None:
                setattr(self, k, v)
