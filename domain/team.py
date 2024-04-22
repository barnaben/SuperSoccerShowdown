from domain.player import Player


class Team:

    def __init__(self):
        self.represented_universe = ''  # Storing the team's represented universe
        self.players = []

    # Set teams's universe
    def set_universe(self, universe):
        self.represented_universe = universe

    # Method to add player to the team
    def add_player(self, player):
        # Add player to the team list
        self.players.append(player)

        # If the team is complete sort the team list based on their height and weight
        if len(self.players) == 5:
            # Sort to get the tallest member to be the goalkeeper
            self.players = sorted(self.players, key=lambda x: x.height, reverse=True)
            # Sort the rest based on their weight. The two heaviest will be the defence
            # The rest is offence
            self.players[1:] = sorted(self.players[1:], key=lambda x: x.weight, reverse=True)

    # Method to remove player from the team
    # Currently not in use
    def remove_player(self, player_to_remove) -> Player | None:
        # Pop the player from the list if the desired index is valid
        if len(self.players) > player_to_remove >= 0:
            return self.players.pop(player_to_remove)
        else:
            return None

    # Method to get the goalkeeper of the team
    def get_goalie(self) -> Player | None:
        # If the team is complete return the first element of the sorted players list
        if len(self.players) == 5:
            return self.players[0]
        return None

    # Method that returns the players in defence
    def get_defence(self) -> list[Player] | None:
        # If the team is complete return the players from index: 1,2 as defence team
        if len(self.players) == 5:
            return self.players[1:3]
        return None

    # Method that returns the players in offence
    def get_offence(self) -> list[Player] | None:
        # If the team is complete return the players from index: 3,4 as offence team
        if len(self.players) == 5:
            return self.players[3:5]
        return None

    def to_dict(self):
        return {"goalkeeper": self.players[0].__dict__,
                "offence": [self.players[1].__dict__, self.players[2].__dict__],
                "defence": [self.players[3].__dict__, self.players[4].__dict__]}

    # Method to pprint the string format of the team
    def __str__(self):
        plot = '---- TEAM LINEUP ---- \n'
        plot += 'Goalie: \n'
        plot += str(self.players[0]) + '\n'
        plot += 'Defence: \n'
        plot += str(self.players[1]) + '\n'
        plot += str(self.players[2]) + '\n'
        plot += 'Offence: \n'
        plot += str(self.players[3]) + '\n'
        plot += str(self.players[4]) + '\n'

        return plot
