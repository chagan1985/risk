from typing import TYPE_CHECKING

from country import Country

class CountryOccupied(Exception):
    """
    Raise this exception when trying to assign a country an owner but the country
    is already occupied by another player
    """
    pass

class CountryNotFound(Exception):
    """
    Raise this exception if the country does not exist on the game board
    """
    pass

class GameLogic:
    def assign_country_owner(country_instance: Country) -> None:
        """
        Checks all of the logic conditions required in order to assign a country
        to a particular player
        """
        if country_instance.country_occupied():
            raise CountryOccupied("This country is already occupied")
        
    def start_game(gameboard_instance) -> None:
        """
        Checks all of the logic conditions required in order to start the main game.
        """
        # Check if all countries are occupied
        if len(gameboard_instance.generate_unoccupied_countries_list()) > 0:
            return False
        
        return True
