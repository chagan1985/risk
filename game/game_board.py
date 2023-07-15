from country import Country
from player import Player

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
        self._board = []
        for country in countries:
            self._board.append(Country(country['name'], country['continent'], country['bordering_countries']))

    def show_list_of_countries(self):
        for country in self._board:
            country.show_country()
