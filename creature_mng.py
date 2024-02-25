from creature import *

class CreatureMng:

    def __init__(self):
        self.creatures = []

    def Add(self, position):
        self.creatures.append(Creature(position))

    def UpdatePaths(self, foodPositions):
        for creature in creatures:
            creature.FindClosestInList(foodPositions)
