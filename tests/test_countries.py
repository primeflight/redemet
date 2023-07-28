import unittest
from redemet.countries import get_countries


class TestGetCountries(unittest.TestCase):
    def test_country_list_length(self):
        countries = get_countries()
        self.assertEqual(len(countries), 203, "The number of countries should be 203")

    def test_country_list_contains(self):
        countries = get_countries()
        self.assertIn("USA", countries, "USA should be in the country list")
        self.assertIn("CANADA", countries, "CANADA should be in the country list")
        self.assertIn("BRAZIL", countries, "BRAZIL should be in the country list")
        self.assertIn("INDIA", countries, "INDIA should be in the country list")

    def test_country_list_unique(self):
        countries = get_countries()
        unique_countries = set(countries)
        self.assertEqual(len(countries), len(unique_countries), "All countries should be unique")

    def test_country_list_case_sensitive(self):
        countries = get_countries()
        self.assertNotIn("usa", countries, "Country names should be case-sensitive")
        self.assertNotIn("brazil", countries, "Country names should be case-sensitive")
