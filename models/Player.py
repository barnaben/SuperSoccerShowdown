# Class for players
class Player:

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def __str__(self):
        return f'Player\'s name: {self.name}, weight: {self.weight}kg, height: {self.height}cm'
