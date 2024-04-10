import math

class Circle:

    def __init__(self, radius:int):
        self.radius = radius

    def get_area(self)->int:
        return math.pi * (self.radius^2) # ^ == **
    def get_perimeter(self)->int:
        return 2 * math.pi * self.radius

