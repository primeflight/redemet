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
