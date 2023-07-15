class Player:
    def __init__(self, name: str, colour: str) -> None:
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
            colour (str): The colour of the player.
        """
        self._name = name
        self._colour = colour

    def show_player(self) -> None:
        """
        Display information about the player.

        This method prints the player's name and the colour they are using.
        """
        print(f"Player {self._name} is using {self._colour}")