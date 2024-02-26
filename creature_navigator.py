#definitions
UP_DIRECTION = [0, 1]
DOWN_DIRECTION = [0, -1]
RIGHT_DIRECTION = [1, 0]
LEFT_DIRECTION = [-1, 0]
STAY_IN_PLACE = [0, 0]
possibleSteps = [UP_DIRECTION, DOWN_DIRECTION, RIGHT_DIRECTION, LEFT_DIRECTION, STAY_IN_PLACE]

def isStepInPathDirection(possibleStep, path):
    return possibleStep[0] * path[0] > 0 or possibleStep[1] * path[1] > 0

class CreatureNavigator:
    def __init__(self, position, home):
        self.position = position
        self.home = home
        self.stepRating = []
        self.path = [0, 0]

    def Move(self, pathMoved):
        self.position = [self.position[0] + pathMoved[0], self.position[1] + pathMoved[1]]

    def Reset(self):
        self.stepRating = []
        self.path = [0, 0]

    def rateSteps(self):
        self.stepRating = []
        for possibleStep in possibleSteps:
            if isStepInPathDirection(possibleStep, self.path):
                self.stepRating.insert(0, possibleStep)
            else:
                self.stepRating.append(possibleStep)

    def NavigateToClosestPossible(self, possibleEnds, stamina):
        closestEnd = self.home
        self.path = [self.home[0] - self.position[0], self.home[1] - self.position[1]]
        homeLength = abs(self.home[0] - self.position[0]) + abs(self.home[1] - self.position[1])
        maxMoves = stamina - homeLength
        minMoves = maxMoves

        for possibleEnd in possibleEnds:
            length = abs(possibleEnd.xPos - self.position[0]) + abs(possibleEnd.yPos - self.position[1])
            if length < minMoves and length < maxMoves:
                minMoves = length
                closestEnd = possibleEnd
                self.path = [possibleEnd.xPos - self.position[0], possibleEnd.yPos - self.position[1]]

        self.rateSteps()

    def IsMoving(self):
        return self.path != STAY_IN_PLACE

    def GetStepsRanking(self):
        return self.stepRating
