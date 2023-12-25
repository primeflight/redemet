#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import helpers.config as config


class Redemet(object):
    def airports(self, api_key: str, country: str):
        """
        @description: API intended to return information
                      on Aerodromes from countries available
                      in the REDEMET database.
        """

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
            raise Exception("Error when making a request to the RedeMet airports country API.")

    def airport_status(self, api_key: str, country: str):
        """
        @description: API intended to return status of
                      locations in colors. The colors
                      are obtained through the evaluation
                      of parameters based on visibility
                      and ceiling of the location.
        """

        params = {
            "api_key": api_key,
            "country": country,
        }

        endpoint = config.ENDPOINT

        response = requests.get(f"{endpoint}/aerodromos/status/pais/{country}", params=params)

        if response.status_code == 200:
            airports = response.json()
            return airports
        else:
            raise Exception(
                "Error when making a request to the RedeMet airports country status API."
            )

    def airport_info(self, api_key: str, location: str):
        """
        @description: Return information on the weather
                      conditions of a location available
                      in the REDEMET database.
        """

        params = {
            "api_key": api_key,
            "localidade": location,
        }

        endpoint = config.ENDPOINT

        response = requests.get(f"{endpoint}/aerodromos/info/", params=params)

        if response.status_code == 200:
            airports = response.json()
            return airports
        else:
            raise Exception(
                "Error when making a request to the RedeMet airports location info API."
            )

    def product_sigwx(self, api_key: str):
        """
        @description: API intended to return the url
                      of the last available low sigwx
                      chart (SUP/FL250).
        """

        params = {
            "api_key": api_key,
        }

        endpoint = config.ENDPOINT

        response = requests.get(f"{endpoint}/produtos/sigwx", params=params)

        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            raise Exception("Error when making a request to the RedeMet products sigwx API.")

    def product_messages_taf(self, api_key: str, locations):
        """
        @description: Return TAF messages from the
                      locations available in the
                      REDEMET database.
        """

        params = {
            "api_key": api_key,
        }

        endpoint = config.ENDPOINT

        locations_str = ",".join(locations)

        response = requests.get(f"{endpoint}/mensagens/taf/{locations_str}", params=params)

        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            raise Exception("Error when making a request to the RedeMet products sigwx API.")

    def product_messages_sigmet(self, api_key: str):
        """
        @description: Return SIGMET messages from the
                      countries available in the REDEMET
                      database.
        """

        params = {
            "api_key": api_key,
        }

        endpoint = config.ENDPOINT

        response = requests.get(f"{endpoint}/mensagens/sigmet", params=params)

        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            raise Exception("Error when making a request to the RedeMet mensagens sigmet API.")

    def product_messages_meteograma(self, api_key: str, locality: str):
        """
        @description: Return information from METAR, TAF
                      and Aerodrome Warning messages for
                      locations available in the REDEMET
                      database.
        """

        params = {
            "api_key": api_key,
        }

        endpoint = config.ENDPOINT

        response = requests.get(f"{endpoint}/mensagens/meteograma/{locality}", params=params)

        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            raise Exception("Error when making a request to the RedeMet mensagens meteograma API.")
