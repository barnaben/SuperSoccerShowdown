import concurrent.futures
import random

import requests

from APIClients.BaseAPICient import BaseAPIClient


# Subclass of BaseAPIClient for fetching Pokémon data
class PokemonAPIClient(BaseAPIClient):
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

        # Base url for the pokémon api
        url = "https://pokeapi.co/api/v2/pokemon/?limit=1025"

        # Fetch pokémon api and get urls from "count" amount of pokémon
        pokemon_data = fetch_url(url)
        random_pokemons = random.sample(pokemon_data["results"], k=count)
        selected_urls = [pokemon["url"] for pokemon in random_pokemons]

        # Concurrently fetching pokémon data for faster execution
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_url, source) for source in selected_urls]
            random_players = [future.result() for future in concurrent.futures.as_completed(futures)]

        # Generating list of pokémons
        players = [{"name": p["name"].title(), "weight": int(p["weight"] / 10), "height": int(p["height"] * 10)} for p
                   in
                   random_players]
        
        return players
