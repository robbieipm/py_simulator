from creature import *

MIN_FOOD_TO_LIVE = 1
MIN_FOOD_TO_REPRODUCE = 2

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
            self.creatures[creatureIdx].MoveTo(newPosition)
            if foodConsumed > 0:
                consumedFoodPositions.append(newPosition)
                self.creatures[creatureIdx].Eat(foodConsumed)
            creatureIdx += 1
        return consumedFoodPositions

    def Size(self):
        return len(self.creatures)

    def EndTurnResult(self):
        deadCreatures = []
        reproducedCreatures = []
        i = 0
        for creature in self.creatures.copy():
            if creature.foodCount < MIN_FOOD_TO_LIVE:
                deadCreatures.append(creature.Position())
                self.creatures.pop(i)
                i -= 1
            elif creature.foodCount >= MIN_FOOD_TO_REPRODUCE:
                reproducedCreatures.append(creature.Position())
            i += 1
        return [deadCreatures, reproducedCreatures]

