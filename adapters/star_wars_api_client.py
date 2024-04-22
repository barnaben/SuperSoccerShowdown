import concurrent.futures
import random

import requests

from interfaces.base_api_client import BaseAPIClient


class StarWarsAPIClient(BaseAPIClient):

    def fetch_players(self, count) -> list[dict]:

        # Function to fetch data from a given url (as source). Returns with the jsonified response
        def fetch_url(source):
            try:
                resp = requests.get(source)
                return resp.json()
            except requests.RequestException as e:
                print(f"Error fetching url: {source}")
                print(e)
                return {}

        # Base url for the star wars api (AT THE TIME OF THE DEVELOPMENT swapi.dev was not available)
        url = "https://www.swapi.tech/api/people/"

        # Fetch star wars api and get urls from "count" amount of character
        star_wars_data = fetch_url(url)
        random_sw_people = random.sample(star_wars_data["results"], k=count)
        selected_urls = [pokemon["url"] for pokemon in random_sw_people]

        # Concurrently fetching star wars data for faster execution
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_url, source) for source in selected_urls]
            random_results = [future.result() for future in concurrent.futures.as_completed(futures)]

        random_players = [prop['result']['properties'] for prop in random_results]

        # Generating list of star wars characters
        players = [{"name": p["name"].title(), "weight": int(p["mass"]), "height": int(p["height"])} for p
                   in
                   random_players]

        return players

    # def fetch_players(self, count) -> list[dict]:
    #     # Base url for Star Wars API
    #     url = "https://swapi.dev/api/people/"
    #
    #     try:
    #         response = requests.get(url)
    #         star_wars_data = response.json()
    #     except requests.RequestException as e:
    #         print(f"Error fetching url: {url}")
    #         print(e)
    #         star_wars_data = []
    #         return star_wars_data
    #
    #     random_players = random.sample(star_wars_data["results"], k=count)
    #     print(random_players)
    #     players = [{"name": p["name"], "weight": int(p["mass"]), "height": int(p["height"])} for p in random_players]
    #     return players
