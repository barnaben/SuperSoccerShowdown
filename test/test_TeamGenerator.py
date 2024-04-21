import unittest
from unittest.mock import Mock

from TeamGenerator import TeamGenerator
from models import Team


class TestTeamGenerator(unittest.TestCase):

    def test_generate_teams(self):
        star_wars_api_client = Mock()
        pokemon_api_client = Mock()

        star_wars_api_client.fetch_players.return_value = [
            {"name": "Luke Skywalker", "height": 172, "weight": 77},
            {"name": "C-3PO", "height": 167, "weight": 75},
            {"name": "R2-D2", "height": 96, "weight": 32},
            {"name": "Darth Vader", "height": 202, "weight": 136},
            {"name": "Leia Organa", "height": 150, "weight": 49}
        ]

        pokemon_api_client.fetch_players.return_value = [
            {"name": "bulbasaur", "weight": 69, "height": 7},
            {"name": "ivysaur", "weight": 130, "height": 10},
            {"name": "venusaur", "weight": 1000, "height": 20},
            {"name": "charmander", "weight": 85, "height": 6},
            {"name": "charmeleon", "weight": 190, "height": 11}
        ]
        team_generator = TeamGenerator([star_wars_api_client, pokemon_api_client], 5)
        teams = team_generator.generate_teams()

        self.assertIsInstance(teams, list)
        self.assertEqual(len(teams), 2)
        self.assertIsInstance(teams[0], Team)


if __name__ == '__main__':
    unittest.main()
