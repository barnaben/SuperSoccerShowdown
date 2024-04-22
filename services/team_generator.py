from domain import Team, Player


class TeamGenerator:

    def __init__(self, team_sources, player_count):
        self.team_sources = team_sources  # List containing the APIClient variants for getting players
        self.player_count = player_count  # Desired number of players in the team, currently not in use

    def generate_teams(self) -> list[Team]:
        # List for containing the teams
        teams = []

        # Generate teams based on the sources
        for team_source in self.team_sources:
            # Get team members for each resource
            players = team_source.fetch_players(self.player_count)
            # Generate teams and add them to the list
            teams.append(self.__get_team(players))

        return teams

    # Method to generate team based on a list of players
    def __get_team(self, players):
        team = Team()
        for person in players:
            player = Player(person["name"], person["weight"], person["height"])
            team.add_player(player)

        return team
