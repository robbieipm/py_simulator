from creature_navigator import *

class Creature:
    def __init__(self, position):
        self.MAX_STAMINA = 10
        self.navigator = CreatureNavigator(position, position)
        self.foodCount = 0
        self.stamina = self.MAX_STAMINA

    def Position(self):
        return self.navigator.position

    def Move(self, pathMoved):
        self.navigator.Move(pathMoved)
        self.stamina -= 1

    def MoveTo(self, pathMoved):
        self.navigator.MoveTo(pathMoved)
        self.stamina -= 1

    def Eat(self, foodAmount):
        self.foodCount += foodAmount

    def Reset(self):
        self.foodCount = 0
        self.navigator.Reset()
        self.stamina = self.MAX_STAMINA

    def FindClosestInList(self, possibleEnds):
        self.navigator.NavigateToClosestPossible(possibleEnds, self.stamina)

    def IsMoving(self):
        return self.navigator.IsMoving()

    def GetStepsRanking(self):
        return self.navigator.GetStepsRanking()
