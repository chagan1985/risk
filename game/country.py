from typing import List

class Country:
    def __init__(self, name: str, continent: str, bordering_countries: List[str]) -> None:
        """
        Initialize a Country object.

        Args:
            name (str): The name of the country.
            continent (str): The continent the country belongs to.
            bordering_countries (list[str]): A list of names of the bordering countries.
        """
        self._name = name
        self._continent = continent
        self._bordering_countries = bordering_countries
        self._owner = None

    def assign_owner(self, player_name) -> None:
        """
        Set the owner name for a particular country
        """
        self._owner = player_name

    def country_occupied(self) -> bool:
        """
        Check if the country is occupied.

        Returns:
            bool: False if the country owner is None, True otherwise.
        """
        return self._owner is not None
    
    def get_name(self) -> str:
        """
        Returns the name of the country.

        Returns:
            str: Name of the country.
        """
        return self._name


    def show_country_information(self) -> None:
        """
        Display information about the country.

        This method returns the name of the country and the continent it belongs to.
        TODO: potentially remove later
        """
        return f"Country {self._name} is in {self._continent}"
