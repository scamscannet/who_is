import dateutil.parser as parser

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


class DatesWrapper(WhoisDataObject):
    formatted: Dates
    raw: Dates

    _fields = {}

    def _parse_date(self, raw_date) -> str | None:
        try:
            return parser.parse(timestr=raw_date).isoformat()
        except parser.ParserError:
            return None

    def __init__(self, whois_dict: dict):
        super().__init__(whois_dict)

        self.raw = Dates(whois_dict=whois_dict)

        parsed_dates = {
            'creation_date': self._parse_date(self.raw.created) if self.raw.created else None,
            'update_date': self._parse_date(self.raw.updated) if self.raw.updated else None,
            'expiration_date': self._parse_date(self.raw.expiration) if self.raw.expiration else None,
        }

        self.formatted = Dates(whois_dict=parsed_dates)

    def json(self) -> dict:
        return {
            'raw': self.raw.json(),
            'formatted': self.formatted.json()
        }