from who_is import whois


def test_query_google_de_recursive():
    result = whois("ctrl-felix.de")
    result_dict = result.json()

    assert result_dict["domain"] == "ctrl-felix.de"
