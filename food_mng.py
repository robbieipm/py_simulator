from food import *

def pop_first_element_conditionally(lst, condition):
    for i in range(len(lst)):  # Iterate over the list in reverse order
        if condition(lst[i]):  # Check if the condition is True for the element
            lst.pop(i)  # If True, pop the element from the list
            return

class FoodMng:

    def __init__(self):
        self.food = []

    def Add(self, position):
        self.food.append(Food(position))

    def FoodPositions(self):
        return self.food

    def Consume(self, consumedFoodPositions):
        if len(consumedFoodPositions) == 0:
            return
        for consumedFoodPos in consumedFoodPositions:
            pop_first_element_conditionally(self.food, lambda x: x.Position() == consumedFoodPos)
