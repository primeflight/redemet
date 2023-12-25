#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import helpers.config as config


class Redemet(object):
    def airports(self, api_key: str, country: str):
        """
        API intended to return information on Aerodromes
        from countries available in the REDEMET database.

        @param api_key
        @param country

        @return
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
            raise Exception("Error when making a request to the RedeMet airports API.")
