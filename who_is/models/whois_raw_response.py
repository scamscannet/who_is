from who_is.models.whois_response import WhoisResponse


class WhoisRawResponse:
    text: str
    whois_server: str

    _raw: str

    def __init__(self, raw_whois: str, whois_server: str):
        self._raw = raw_whois
        self.whois_server = whois_server
        self._format()
        self._whois_to_kv()

    def _format(self):
        # Remove \r to have only \n as linebreaks in the whois text
        w = self._raw.replace("\r", "")

        self.text = w

    def _whois_to_kv(self):
        parsed_data = dict(whois_server=self.whois_server)
        current_key = ""

        for line in self.text.split("\n"):
            if ":" in line and not current_key:
                key, value = line.strip().split(":", 1)

                formatted_key = key.replace(" ", "_").lower()
                formatted_value = value.strip()

                if formatted_key not in parsed_data:
                    parsed_data[formatted_key] = formatted_value
                elif isinstance(parsed_data[formatted_key], list):
                    parsed_data[formatted_key].append(formatted_value)
                else:
                    parsed_data[formatted_key] = [parsed_data[formatted_key], formatted_value]

            else:
                pass

        self._kv = parsed_data

    def __str__(self):
        return self.text

    def json(self):
        return self._kv

    def format(self) -> WhoisResponse:
        return WhoisResponse(whois_dict=self.json(), raw=self._raw)
