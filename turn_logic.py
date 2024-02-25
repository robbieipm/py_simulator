from grid import *
from creature_mng import *
from food_mng import *
from terminal_printer import *

class TurnLogic:

    def __init__(self, grid, creatureMng, foodMng, printer):
        # definitions
        self.CREATURE_INIT_SPAWN = 1
        self.FOOD_INIT_SPAWN = self.CREATURE_INIT_SPAWN * 2
        # initializing
        self.grid = grid
        self.creatureMng = creatureMng
        self.foodMng = foodMng
        self.printer = printer
        self.grid.PrintGrid()
        self.Init()
        self.printer.RewriteGrid()

    def Init(self):
        for _ in range(self.CREATURE_INIT_SPAWN):
            emptyTile = self.grid.GetEmptyTile()
            if emptyTile.Type() == Tile.INVALID_TYPE:
                self.printer.PrintError("was unable to spawn creature")
            emptyTile.ChangeType(Tile.CREATURE_TYPE)
            self.creatureMng.Add(emptyTile.Position())

        for _ in range(self.FOOD_INIT_SPAWN):
            emptyTile = self.grid.GetEmptyTile()
            if emptyTile.Type() == Tile.INVALID_TYPE:
                self.printer.PrintError("was unable to spawn food")
            emptyTile.ChangeType(Tile.FOOD_TYPE)
            self.foodMng.Add(emptyTile.Position())

        self.printer.RewriteGrid()
        # TODO: record turn 0

    def Start(self, turnNumber):
        # move creatures to food and back home
        self.movementStage()
        # pause?
        # remove uneaten food
        # remove dead creatures
        # spawn born creatures

    def movementStage(self):
        self.creatureMng.UpdatePaths(self.foodMng.FoodPositions())
        