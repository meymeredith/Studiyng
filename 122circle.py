import math

class Circle:
    def __init__(self, r):
        self.r = r
    def getLenght(self):
        return 2 * math.pi * self.r
    def getSquare(self):
        return math.pi * self.r * self.r

circle1 = Circle(5)
print(circle1.getLenght())
print(circle1.getSquare())
