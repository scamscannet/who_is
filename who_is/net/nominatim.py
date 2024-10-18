import requests

from who_is.exceptions.geocoding import GeocodingFailure


def query_unformatted_address(query: str) -> dict:
    url = "https://nominatim.openstreetmap.org"

    response = requests.get(
        url + "/search",
        params={
            "q": query,
            "format": "jsonv2",
            "addressdetails": 1
        },
        headers={
            "User-Agent": "scamscannet/who-is"
        }
    )
    response_data = response.json()

    if not response_data:
        raise GeocodingFailure()
    
    picked_address = response_data[0]["address"]

    address_dict = {
        'street': picked_address["road"] if "road" in picked_address else None,
        'house_number': picked_address["house_number"] if "house_number" in picked_address else None,
        'city': picked_address["town"] if "town" in picked_address else None,
        'state': picked_address["state"] if "state" in picked_address else None,
        'postal_code': picked_address["postcode"] if "postcode" in picked_address else None,
        'country': picked_address["country"] if "country" in picked_address else None,
        'country_code': picked_address["country_code"].upper() if "country_code" in picked_address else None,
    }

    return address_dict

