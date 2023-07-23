import pytest

from game.country import Country

TEST_COUNTRY = {
    "name": "Japan",
    "continent": "Asia",
    "bordering_countries": ["Kamchatka", "Mongolia"]
}

class TestCountry:
    def test_create(self):
        """ Test player init """
        country_instance = Country(
            name=TEST_COUNTRY["name"],
            continent=TEST_COUNTRY["continent"],
            bordering_countries=TEST_COUNTRY["bordering_countries"]
        )
        assert country_instance._name == TEST_COUNTRY["name"]
        assert country_instance._bordering_countries == TEST_COUNTRY["bordering_countries"]
        assert country_instance._continent == TEST_COUNTRY["continent"]
        assert country_instance._owner == None

    def test_assign_owner(self):
        """ Test assigning an owner to a country """
        test_player = "player1"

        country_instance = Country(
            name=TEST_COUNTRY["name"],
            continent=TEST_COUNTRY["continent"],
            bordering_countries=TEST_COUNTRY["bordering_countries"]
        )
        assert country_instance._owner == None

        country_instance.assign_owner(test_player)
        assert country_instance._owner == test_player

    def test_country_occupied(self):
        """ Test the country occupied value before and after owner assignment """
        test_player = "player1"

        country_instance = Country(
            name=TEST_COUNTRY["name"],
            continent=TEST_COUNTRY["continent"],
            bordering_countries=TEST_COUNTRY["bordering_countries"]
        )
        assert country_instance.country_occupied() == False

        country_instance.assign_owner(test_player)
        assert country_instance.country_occupied() == True

    def test_get_country_name(self):
        """ Test getting the name of the country """
        country_instance = Country(
            name=TEST_COUNTRY["name"],
            continent=TEST_COUNTRY["continent"],
            bordering_countries=TEST_COUNTRY["bordering_countries"]
        )

        assert country_instance.get_name() == TEST_COUNTRY["name"]

    def test_show_country_information(self):
        """ Test the show country information """
        expected_show_country_message = f"Country {TEST_COUNTRY['name']} is in {TEST_COUNTRY['continent']}"

        country_instance = Country(
            name=TEST_COUNTRY["name"],
            continent=TEST_COUNTRY["continent"],
            bordering_countries=TEST_COUNTRY["bordering_countries"]
        )
        
        country_info = country_instance.show_country_information()
        assert country_info == expected_show_country_message
