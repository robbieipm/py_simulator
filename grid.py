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

        return Tile(-1, -1, Tile.INVALID_TYPE)

    def GetEmptyTileAround(self, source):
        possibleTiles = []
        if source[0] > 0:
            possibleTiles.append([source[0] - 1, source[1]])
        if source[0] < self.width - 1:
            possibleTiles.append([source[0] + 1, source[1]])
        if source[1] > 0:
            possibleTiles.append([source[0], source[1] - 1])
        if source[1] < self.height - 1:
            possibleTiles.append([source[0], source[1] + 1])

        if len(possibleTiles) == 0:
            return Tile(-1, -1, Tile.INVALID_TYPE)
        random.shuffle(possibleTiles)
        for possibleTilePos in possibleTiles:
            possibleTile = self.grid[possibleTilePos[0]][possibleTilePos[1]]
            if possibleTile.Type() == Tile.EMPTY_TYPE:
                return possibleTile

        return Tile(-1, -1, Tile.INVALID_TYPE)

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

    def isValidPosition(self, position):
        return position[0] >= 0 and position[0] < self.width and position[1] >= 0 and position[1] < self.height

    def ExecuteMovements(self, navigationPossibilities):
        executedMovements = []
        for movement in navigationPossibilities:
            food = 0
            oldPosition = movement[0]
            ratedSteps = movement[1]
            for i in range(len(ratedSteps)):
                newPosition = [oldPosition[0] + ratedSteps[i][0], oldPosition[1] + ratedSteps[i][1]]
                if not self.isValidPosition(newPosition):
                    continue
                if self.IsType(Tile.EMPTY_TYPE, newPosition) or newPosition == oldPosition:
                    break
                elif self.IsType(Tile.FOOD_TYPE, newPosition):
                    food += 1
                    break

            executedMovements.append([newPosition, food])
            self.grid[oldPosition[0]][oldPosition[1]].ChangeType(Tile.EMPTY_TYPE)
            self.grid[newPosition[0]][newPosition[1]].ChangeType(Tile.CREATURE_TYPE)
        return executedMovements

    def ResetTiles(self, tilePositions):
        for tilePos in tilePositions:
            self.grid[tilePos[0]][tilePos[1]].ChangeType(Tile.EMPTY_TYPE)
