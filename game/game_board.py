import logging
from typing import List

from country import Country
from game_logic import (
    GameLogic, CountryNotFound, CountryOccupied
)
from player import Player

logging.basicConfig(filename='game.log', level=logging.INFO)

# TODO make a JSON file to hold country data as this should never change
countries = [
    {
        "name": "Japan",
        "continent": "Asia",
        "bordering_countries": ["Kamchatka", "Mongolia"],
    },
    {
        "name": "Mongolia",
        "continent": "Asia",
        "bordering_countries": ["Kamchatka", "Japan", "China", "Siberia", "Irkutsk"],
    },
]

class GameBoard:
    def __init__(self) -> None:
        """Initialize the Game object."""
        self._board = []
        self._players = []
        self._game_logic = GameLogic()
        for country in countries:
            self._board.append(Country(country['name'], country['continent'], country['bordering_countries']))

    def assign_country(self, country_name: str, player_name: str) -> None:
        """Assign a country to a player.

        Args:
            country_name (str): The name of the country to be assigned.
            player_name (str): The name of the player who will be assigned the country.

        Raises:
            CountryNotFound: If the country does not exist on the game board.
            CountryOccupied: If the country is already assigned to a player.
        """
        try:
            country_instance = self.find_country_on_board(country_name)
            self._game_logic.assign_country_owner(country_instance)
            country_instance.assign_owner(player_name)
        except (CountryNotFound, CountryOccupied) as error:
            logging.error(error)

    def find_country_on_board(self, country_name: str) -> Country:
        """Find a country on the game board.

        Args:
            country_name (str): The name of the country to find.

        Returns:
            Country: The Country object representing the found country.

        Raises:
            CountryNotFound: If the country does not exist on the game board.
        """
        for country in self._board:
            if country.get_name() == country_name:
                return Country
        
        raise CountryNotFound(f"The country {country_name} does not exist on the game board")

    def generate_unoccupied_countries_list(self) -> List[str]:
        """Generate a list of unoccupied countries on the game board.

        Returns:
            List[str]: A list of country names that are unoccupied.
        """
        unoccupied_countries = []
        for country in self._board:
            if not country.country_occupied():
                unoccupied_countries.append(country.get_name())

        return unoccupied_countries

    def show_list_of_unoccupied_countries(self) -> None:
        """Display a list of unoccupied countries on the game board."""
        print('List of unoccupied countries:')
        print(', '.join(self.generate_unoccupied_countries_list()))

    def check_game_start(self) -> None:
        """Check if the game can start based on the game logic.

        Whether the conditions are met to start the game or not.
        """
        if self._game_logic.start_game():
            print('Conditions met to start the game')
        else:
            print('Conditions not yet met to start the game')
