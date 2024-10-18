from who_is.models.generics.whois_data_object import WhoisDataObject, WhoisDataField


class General(WhoisDataObject):
    domain: str
    name_servers: list = []
    status: list = []

    _fields = {
        'domain': WhoisDataField(matching_keys=['domain_name']),
        'name_servers': WhoisDataField(matching_keys=['name_server', 'nserver'], data_type=list),
        'status': WhoisDataField(matching_keys=['domain_status'], data_type=list),
    }