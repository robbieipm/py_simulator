class Food:
    def __init__(self, position):
        self.xPos = position[0]
        self.yPos = position[1]

    def Position(self):
        return [self.xPos, self.yPos]
