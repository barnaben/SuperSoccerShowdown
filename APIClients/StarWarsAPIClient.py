import random

import requests

from APIClients.BaseAPICient import BaseAPIClient


class StarWarsAPIClient(BaseAPIClient):

    def fetch_players(self, count) -> list[dict]:
        # Base url for Star Wars API
        url = "https://swapi.dev/api/people/"

        try:
            response = requests.get(url)
            star_wars_data = response.json()
        except requests.RequestException as e:
            print(f"Error fetching url: {url}")
            print(e)
            star_wars_data = {}

        random_players = random.sample(star_wars_data["results"], k=count)

        players = [{"name": p["name"], "weight": int(p["mass"]), "height": int(p["height"])} for p in random_players]
        return players
