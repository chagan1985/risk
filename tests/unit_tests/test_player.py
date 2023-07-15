import pytest

from game.player import Player

class TestPlayer:
    def test_create(self):
        ''' Test player init '''
        player = Player("Chris", "Red")
        assert player._name == "Chris"
        assert player._colour == "Red"

    def test_show_player(self, capfd):
        ''' Test show_player produces the expected print statement '''
        test_name = "Chris"
        test_colour = "Orange"
        expected_player_text = f"Player {test_name} is using {test_colour}"

        player = Player(test_name, test_colour)
        player.show_player()

        captured = capfd.readouterr()
        show_player_text = captured.out.strip()

        assert show_player_text == expected_player_text
