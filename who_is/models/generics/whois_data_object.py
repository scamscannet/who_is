import typing

import validators
from validators import ValidationError


class WhoisDataField:
    matching_keys = [""]
    validator = None
    data_type: type = str

    def __init__(self, matching_keys: list, validator: str = None, data_type: type = str):
        self.validator = validator
        self.matching_keys = matching_keys
        self.data_type = data_type


class WhoisDataObject:
    _fields: typing.Dict[str, WhoisDataField] = {}

    def __init__(self, whois_dict: dict):

        for key, parsing_data in self._fields.items():
            validator = getattr(validators, parsing_data.validator) if parsing_data.validator and hasattr(
                validators, parsing_data.validator) else None

            # Skip matching if data is a nested type

            if issubclass(parsing_data.data_type, WhoisDataObject):
                obj = parsing_data.data_type(whois_dict)

                setattr(self, key, obj)
                continue

            matching_keys = parsing_data.matching_keys
            matches = [x for x in matching_keys if x in whois_dict]

            if not matches:
                for mk in matching_keys:
                    for k in whois_dict:
                        if mk in k:
                            matches.append(k)

            value_added = False
            for match in matches:
                if validator:
                    result = validator(whois_dict[match])
                    if isinstance(result, ValidationError):
                        continue

                if parsing_data.data_type == list:
                    if isinstance(whois_dict[match], list):
                        setattr(self, key, getattr(self, key) + whois_dict[match])
                    else:
                        getattr(self, key).append(whois_dict[match])
                else:
                    setattr(self, key, whois_dict[match])


                value_added = True
                break

            if not value_added:
                setattr(self, key, None)

    def __iter__(self):
        return iter(self._fields)

    def __getitem__(self, key):
        return getattr(self, key)

    def json(self) -> dict:
        data = {}
        for key in self._fields.keys():
            value = getattr(self, key)
            if isinstance(value, WhoisDataObject):
                value = value.json()
            data[key] = value

        return data
