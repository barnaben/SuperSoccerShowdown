import random
import unittest

from domain import Player, Team


class TestTeam(unittest.TestCase):

    def setUp(self):
        test_team = [
            {"name": "bulbasaur", "weight": 69, "height": 7},  # Offence
            {"name": "ivysaur", "weight": 130, "height": 10},  # Defence
            {"name": "venusaur", "weight": 1000, "height": 20},  # Goalie
            {"name": "charmander", "weight": 85, "height": 6},  # Offence
            {"name": "charmeleon", "weight": 190, "height": 11}]  # Defence
        self.players = []
        for person in test_team:
            self.players.append(Player(person["name"], person["weight"], person["height"]))

        self.team = Team()

    def test_add_player(self):
        for index, player in enumerate(self.players):
            self.team.add_player(player)
            self.assertEqual(len(self.team.players), index + 1)
            self.assertTrue(player in self.team.players)

    def test_get_goalie(self):
        self.assertIsNone(self.team.get_goalie())
        for index, player in enumerate(self.players):
            self.team.add_player(player)
        self.assertEqual(self.team.get_goalie(), self.players[2])

    def test_get_defence(self):
        self.assertIsNone(self.team.get_defence())

        for index, player in enumerate(self.players):
            self.team.add_player(player)

        self.assertTrue(len(self.team.get_defence()) == 2)
        self.assertEqual(self.team.get_defence(), [self.players[4], self.players[1]])

    def test_get_offence(self):
        self.assertIsNone(self.team.get_offence())

        for index, player in enumerate(self.players):
            self.team.add_player(player)

        self.assertTrue(len(self.team.get_offence()) == 2)
        self.assertEqual(self.team.get_offence(), [self.players[3], self.players[0]])

    def test_remove_player(self):
        while len(self.team.players) != 0:
            num_players = len(self.team.players)
            player_index = random.choice(range(len(self.team.players)))
            player_to_remove = self.team.players[player_index]

            self.assertEqual(self.team.remove_player(player_index), player_to_remove)
            self.assertEqual(len(self.team.players), num_players - 1)

        self.assertIsNone(self.team.remove_player(0))


if __name__ == '__main__':
    unittest.main()
