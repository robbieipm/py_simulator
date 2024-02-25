class Creature:
    def __init__(self, position):
        self.xPos = position[0]
        self.yPos = position[1]
        self.home = position
        self.foodCount = 0
        self.path = [0, 0]
        self.stamina = 10

    def Position(self):
        return [self.xPos, self.yPos]

    def Move(self, pathMoved):
        self.xPos = self.xPos + pathMoved[0]
        self.yPos = self.yPos + pathMoved[1]

    def Eat(self, foodAmount):
        self.foodCount += foodAmount

    def Reset(self):
        self.foodCount = 0
        self.path = [0, 0]

    def FindClosestInList(self, possibleEnds):
        closestEnd = self.home
        self.path = [self.home[0] - self.xPos, self.home[1] - self.yPos]
        homeLength = abs(self.home[0] - self.xPos) + abs(self.home[1] - self.yPos)
        minMoves = -1
        maxMoves = self.stamina - homeLength

        for possibleEnd in possibleEnds:
            length = abs(possibleEnd.xPos - self.xPos) + abs(possibleEnd.yPos - self.yPos)
            if length < minMoves or minMoves < 0 and length < maxMoves:
                minMoves = length
                closestEnd = possibleEnd
                self.path = [possibleEnd.xPos - self.xPos, possibleEnd.yPos - self.yPos]
