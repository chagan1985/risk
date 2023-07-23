from typing import Literal

class Player:
    def __init__(self, name: str, colour: str, player_type: Literal['USER', 'CPU']) -> None:
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
            colour (str): The colour of the player.
            player_type (Literal['USER', 'CPU']): The type of the player, which can be 'USER' or 'CPU'.
        """
        self._name = name
        self._colour = colour
        self._player_type = player_type

    def show_player(self) -> None:
        """
        Display information about the player.

        This method prints the player's name and the colour they are using.
        """
        print(f"Player {self._name} is using {self._colour}")
