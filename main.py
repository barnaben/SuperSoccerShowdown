from flask import Flask, jsonify

from adapters import StarWarsAPIClient, PokemonAPIClient
from application import TeamGenerator

app = Flask(__name__)

# Get api clients
star_wars_api_client = StarWarsAPIClient()
pokemon_api_client = PokemonAPIClient()

# Number of players in the team
# NOT FULLY IMPLEMENTED, ONLY 5 IS ACCEPTED
num_players = 5

# Create team generator
team_generator = TeamGenerator([star_wars_api_client, pokemon_api_client], num_players)


@app.route('/', methods=['GET'])
def super_soccer_showdown():
    # Create teams
    teams = team_generator.generate_teams()

    # Convert teams to JSON format
    json_teams = []
    for i, team in enumerate(teams, start=1):
        json_team = {'team_number': i, 'players': team.to_dict()}
        json_teams.append(json_team)

    return jsonify(json_teams)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
