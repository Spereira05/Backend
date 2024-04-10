import unittest
import math

class Circle:

    def __init__(self, radius:int):
        self.radius = radius

    def get_area(self)->int:
        return math.pi * (self.radius^2) # ^ == **
    def get_perimeter(self)->int:
        return 2 * math.pi * self.radius



class CircleTests(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle (radius = 4)

    def test_calculate_area(self):

        assert 50,265 == round(self.circle.area, 3)

    def test_calculate_perimeter(self):

        assert 25,133 == round(self.circle.perimeeter, 3)

if __name__ =="__main__":
    unittest.main()