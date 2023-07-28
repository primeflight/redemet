import unittest
import airfields


class TestAirfields(unittest.TestCase):
    def test_get_airports_successful(self):
        api_key = "424f75d08159469ea32820d7436e4684"
        country = "Brazil"

        airports = airfields.get_airports(api_key, country)

        self.assertIsInstance(airports, list)
        self.assertGreater(len(airports), 0)

    def test_get_airports_invalid_country(self):
        api_key = "424f75d08159469ea32820d7436e4684"
        country = "InvalidCountry"

        with self.assertRaises(Exception):
            airfields.get_airports(api_key, country)


if __name__ == "__main__":
    unittest.main()
