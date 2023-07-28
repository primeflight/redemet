import unittest
import airfields
import mock


class TestAirfields(unittest.TestCase):
    @mock.patch.object(airfields, "get_airports")
    def test_get_airports_successful(self, mock_get_airports):
        api_key = "424f75d08159469ea32820d7436e4684"
        country = "Brazil"

        mock_get_airports.return_value = [
            {
                "id": 3226,
                "cod": "SBAA",
                "nome": "Aeroporto de Conceição do Araguaia",
                "cidade": "Conceicao do Araguaia/PA",
                "pais": "BRASIL",
                "lat_grau": "8",
                "lat_min": "20",
                "lat_sec": "54",
                "lat_dir": "S",
                "lon_grau": "49",
                "lon_min": "18",
                "lon_sec": "5",
                "lon_dir": "W",
                "altitude_pes": 653,
                "lat_dec": "-8.34833",
                "lon_dec": "-49.3014",
                "altitude_metros": 199,
            },
            {
                "id": 3227,
                "cod": "SBAC",
                "nome": "Aeroporto Dragão do Mar",
                "cidade": "Aracati",
                "pais": "BRASIL",
                "lat_grau": "",
                "lat_min": "",
                "lat_sec": "",
                "lat_dir": "",
                "lon_grau": "",
                "lon_min": "",
                "lon_sec": "",
                "lon_dir": "",
                "altitude_pes": 128,
                "lat_dec": "-4.56861",
                "lon_dec": "-37.8047",
                "altitude_metros": 23,
            },
            {
                "id": 3228,
                "cod": "SBAE",
                "nome": "Aeroporto Internacional Bauru-Arealva / Moussa Nak",
                "cidade": "Bauru/SP",
                "pais": "BRASIL",
                "lat_grau": "22",
                "lat_min": "9",
                "lat_sec": "41",
                "lat_dir": "S",
                "lon_grau": "49",
                "lon_min": "4",
                "lon_sec": "12",
                "lon_dir": "W",
                "altitude_pes": 1949,
                "lat_dec": "-22.1585",
                "lon_dec": "-49.0735",
                "altitude_metros": 594,
            },
        ]

        airports = airfields.get_airports(api_key, country)

        self.assertEqual(mock_get_airports.call_count, 1)
        self.assertEqual(airports, mock_get_airports.return_value)

    @mock.patch.object(airfields, "get_airports")
    def test_get_airports_invalid_country(self, mock_get_airports):
        api_key = "424f75d08159469ea32820d7436e4684"
        country = "InvalidCountry"

        mock_get_airports.side_effect = Exception("Invalid country")

        with self.assertRaises(Exception):
            airfields.get_airports(api_key, country)

        self.assertEqual(mock_get_airports.call_count, 1)


if __name__ == "__main__":
    unittest.main()
