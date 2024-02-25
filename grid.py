import random
from tile import *
from food import *
from creature import *

class Grid:

    def __init__(self, height = 10, width = 10):
        self.height = height
        self.width = width
        self.grid = []
        self.maxTiles = self.height * self.width
        self.randomTile = [i for i in range(0, self.maxTiles)]
        random.shuffle(self.randomTile)

        for i in range(self.height):
            self.grid.append([])
            for j in range (self.width):
                self.grid[i].append(Tile(i, j))

    def PrintGrid(self):
        for row in self.grid:
            rowString = " ".join(str(tile) for tile in row)
            print(rowString, end="\n", flush=True)

    def getRandomTile(self):
        chosenTile = self.randomTile.pop(0)
        self.randomTile.append(chosenTile)

        return self.grid[int(chosenTile / self.width)][chosenTile % self.height]

    def GetEmptyTile(self):
        for _ in range(self.maxTiles):
            emptyTile = self.getRandomTile()
            if emptyTile.Type() == Tile.EMPTY_TYPE:
                return emptyTile

        return Tile(-1, -1, "invalid")

    def Spawn(self, spawnType):
        emptyTile = self.GetEmptyTile()
        if emptyTile.Type() == Tile.INVALID_TYPE:
            return None
        emptyTile.ChangeType(spawnType)

        spawnedPos = emptyTile.Position()
        if spawnType == Tile.FOOD_TYPE:
            return Food(spawnedPos[0], spawnedPos[1])
        if spawnType == Tile.CREATURE_TYPE:
            return Creature(spawnedPos[0], spawnedPos[1])

        return spawnedElement

    def IsType(self, tileType, position):
        return tileType == self.grid[position[0]][position[1]].Type()

    def getStepPosition(self, path):
        xChange = 0
        yChange = 0
        if path[0] > 0:
            xChange = 1
        elif path[0] < 0:
            xChange = -1
        elif path[1] > 0:
            yChange = 1
        else:
            yChange = -1

        return [xChange, yChange]

    def MoveCreature(self, creature):
        if creature.path == [0, 0]:
            return True
        creaturePosition = creature.Position()
        stepPosition = self.getStepPosition(creature.path)
        newPosition = [creaturePosition[0] + stepPosition[0], creaturePosition[1] + stepPosition[1]]
        # check if wanted tile is free
        if not self.IsType(Tile.EMPTY_TYPE, newPosition):
            if self.IsType(Tile.FOOD_TYPE , newPosition):
                print("ATE!!")
                creature.Eat(1)
                #TODO: remove food
            else:
                print("BLOCKED!")
                return False

        self.grid[creature.xPos][creature.yPos].ChangeType(Tile.EMPTY_TYPE)
        creature.path = [creature.path[0] - stepPosition[0], creature.path[1] - stepPosition[1]]
        print(f"before position: {creature.Position()}")
        creature.Move(stepPosition)
        print(f"after position: {creature.Position()}")
        self.grid[creature.xPos][creature.yPos].ChangeType(Tile.CREATURE_TYPE)
        return True

