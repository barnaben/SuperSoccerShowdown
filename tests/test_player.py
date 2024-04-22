import unittest

from domain import Player


class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        test_cases = [
            {"name": "Luke Skywlaker", "weight": 77, "height": 172},
            {"name": "C-3PO", "weight": 167, "height": 75},
            {"name": "R2-D2", "weight": 96, "height": 32}]

        for test in test_cases:
            player = Player(test["name"], test["weight"], test["height"])
            self.assertEqual(player.name, test["name"])
            self.assertEqual(player.weight, test["weight"])
            self.assertEqual(player.height, test["height"])

    def test_player_string_representation(self):
        test_cases = [
            {"name": "bulbasaur", "weight": 69, "height": 7},
            {"name": "ivysaur", "weight": 130, "height": 10},
            {"name": "venusaur", "weight": 1000, "height": 20}]

        for test in test_cases:
            player = Player(test["name"], test["weight"], test["height"])
            self.assertEqual(str(player),
                             f'Player\'s name: {test["name"]}, weight: {test["weight"]}kg, height: {test["height"]}cm')


if __name__ == '__main__':
    unittest.main()
