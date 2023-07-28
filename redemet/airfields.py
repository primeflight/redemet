import requests
import helpers.config as config


def get_airports(api_key, country):
    params = {
        "api_key": api_key,
        "country": country,
    }

    endpoint = config.ENDPOINT

    response = requests.get(f"{endpoint}/aerodromos/", params=params)

    if response.status_code == 200:
        airports = response.json()
        return airports
    else:
        raise Exception("Error when making a request to the RedeMet airports API.")
