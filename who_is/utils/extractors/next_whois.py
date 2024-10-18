import validators


def next_whois_server(whois_dict: dict, exclude: list) -> str:
    search_keys = ["whois", "refer"]
    keys = [k for k in whois_dict.keys() if any(sk in k for sk in search_keys)]

    matches = []
    for key in keys:
        value = whois_dict[key]

        if value in exclude:
            continue

        result = validators.domain(value)
        if isinstance(result, validators.ValidationError):
            continue

        if "/" in value:
            continue

        matches.append(value)

    if len(matches) > 0:
        return matches[0]
