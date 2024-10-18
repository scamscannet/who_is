from who_is import whois


def test_query_google_com_recursive():
    result = whois("google.com")
    result_dict = result.json()

    assert result_dict["registrar"]["iana_id"] == "292"
