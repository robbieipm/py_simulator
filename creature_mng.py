from creature import *

class CreatureMng:

    def __init__(self):
        self.creatures = []
        self.movingCreatures = []

    def Add(self, position):
        self.creatures.append(Creature(position))

    def UpdatePaths(self, foodPositions):
        for creature in self.creatures:
            creature.FindClosestInList(foodPositions)

    def PrepareToMove(self, foodPositions):
        for creature in self.creatures:
            creature.Reset()
        if len(self.creatures) > 0:
            self.movingCreatures = [i for i in range(0, len(self.creatures))]
        self.UpdatePaths(foodPositions)

    def AreCreaturesStillMoving(self):
        stillMovingCreatures = []
        for i in self.movingCreatures:
            if self.creatures[i].IsMoving():
                stillMovingCreatures.append(i)
        self.movingCreatures = stillMovingCreatures.copy()
        return len(self.movingCreatures) > 0

    def GetOptionalMovements(self):
        optionalMovements = []
        for creature in self.creatures:
            optionalMovements.append([creature.Position(), creature.GetStepsRanking()])
        return optionalMovements

    def MoveCreatures(self, movementsInfo):
        consumedFoodPositions = []
        creatureIdx = 0
        for info in movementsInfo:
            newPosition = info[0]
            foodConsumed = info[1]
            self.creatures[creatureIdx].Move(newPosition)
            if foodConsumed > 0:
                consumedFoodPositions.append(newPosition)
                self.creatures[creatureIdx].Eat(foodConsumed)
            creatureIdx += 1
        return consumedFoodPositions
