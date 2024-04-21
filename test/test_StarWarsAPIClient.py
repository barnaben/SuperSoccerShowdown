import unittest

from APIClients import StarWarsAPIClient


class TestStarWarsAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = StarWarsAPIClient()

    def test_fetch_players(self):
        players = self.client.fetch_players(5)
        self.assertTrue(len(players) == 5)
        self.assertCountEqual(["name", "weight", "height"], players[0].keys())

        players = self.client.fetch_players(7)
        self.assertTrue(len(players) == 7)
        self.assertCountEqual(["name", "weight", "height"], players[0].keys())
        self.assertIsInstance(players[0]["name"], str)
        self.assertIsInstance(players[0]["weight"], int)
        self.assertIsInstance(players[0]["weight"], int)


if __name__ == '__main__':
    unittest.main()
