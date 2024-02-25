class Tile:
    emptyTileSymbol = "_"
    invalidTileSymbol = "X"
    creatureTileSymbol = "O"
    foodTileSymbol ="."
    EMPTY_TYPE = "empty"
    INVALID_TYPE = "invalid"
    CREATURE_TYPE = "creature"
    FOOD_TYPE = "food"

    def __init__(self, xPos, yPos, tileType = "empty"):
        self.xPos = xPos
        self.yPos = yPos
        self.typeSymbol = self.invalidTileSymbol
        self.type = self.GetType(tileType)

    def GetType(self, tileType):
        if tileType.lower() == self.FOOD_TYPE or tileType.lower() == "f":
            self.typeSymbol = self.foodTileSymbol
            return self.FOOD_TYPE
        elif tileType.lower() == self.CREATURE_TYPE or tileType.lower() == "c":
            self.typeSymbol = self.creatureTileSymbol
            return self.CREATURE_TYPE
        elif tileType.lower() == self.INVALID_TYPE or tileType.lower() == "x":
            self.typeSymbol = self.invalidTileSymbol
            return self.INVALID_TYPE

        self.typeSymbol = self.emptyTileSymbol
        return self.EMPTY_TYPE

    def Type(self):
        return self.type

    def Position(self):
        return (self.xPos, self.yPos)

    def ChangeType(self, newType):
        self.type = self.GetType(newType)

    def __str__(self):
        return f'{self.typeSymbol}'