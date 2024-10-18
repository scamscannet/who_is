from who_is.models.generics.whois_data_object import WhoisDataObject, WhoisDataField


class Dates(WhoisDataObject):
    created: str
    updated: str
    expiration: str

    _fields = {
        "created": WhoisDataField(matching_keys=["creation_date"]),
        "updated": WhoisDataField(matching_keys=["update_date", "updated_date"]),
        "expiration": WhoisDataField(matching_keys=["expiration_date", "expiration", "expiry"])
    }
