import requests
from redemet.countries import get_countries
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_parallel_requests(url, api_key, countries):
    base_url = f"{url}/?api_key={api_key}&pais="

    def fetch(country):
        response = requests.get(base_url + country)
        return country, response.status_code

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(fetch, country): country for country in countries}

        failed_countries = []
        for future in as_completed(futures):
            country, status_code = future.result()
            if status_code != 200:
                failed_countries.append(country)

    return failed_countries


# URL e chave da API (substitua pela URL real e chave da API, se necessário)
url = "https://api-redemet.decea.mil.br/aerodromos"
api_key = ""

countries_list = get_countries()
failed_countries_list = make_parallel_requests(url, api_key, countries_list)
