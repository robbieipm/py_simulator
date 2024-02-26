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
    def __init__(self, position):
        self.position = position
        self.stepRating = []
        self.path = [0, 0]

    def Move(self, pathMoved):
        self.position = [self.position[0] + pathMoved[0], self.position[1] + pathMoved[1]]

    def MoveTo(self, newPosition):
        self.position = [newPosition[0], newPosition[1]]

    def Reset(self):
        self.stepRating = []
        self.path = [0, 0]

    def rateSteps(self):
        self.stepRating = []
        if self.path == STAY_IN_PLACE:
            self.stepRating.append(STAY_IN_PLACE)
            return
        for possibleStep in possibleSteps:
            if isStepInPathDirection(possibleStep, self.path):
                self.stepRating.insert(0, possibleStep)
            else:
                self.stepRating.append(possibleStep)

    def NavigateToClosestPossible(self, possibleEnds, stamina):
        closestEnd = self.position
        self.path = STAY_IN_PLACE
        maxMoves = stamina
        minMoves = maxMoves

        for possibleEnd in possibleEnds:
            length = abs(possibleEnd[0] - self.position[0]) + abs(possibleEnd[1] - self.position[1])
            if length < minMoves and length < maxMoves:
                minMoves = length
                closestEnd = possibleEnd
                self.path = [possibleEnd[0] - self.position[0], possibleEnd[1] - self.position[1]]

        self.rateSteps()

    def IsMoving(self):
        return self.path != STAY_IN_PLACE

    def GetStepsRanking(self):
        return self.stepRating
