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

    def show_country(self) -> None:
        """
        Display information about the country.

        This method prints the name of the country and the continent it belongs to.
        """
        print(f"Country {self._name} is in {self._continent}")
