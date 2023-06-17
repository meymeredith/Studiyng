class Square():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def squareSquare(self):
        return self.length * self.width
        
class Cube(Square):
    def __init__(self,length,width,heigth):
        Square.__init__(self,length,width)
        self.heigth = heigth
    def cubeVolume(self):
        return Square.squareSquare(self) * self.heigth

cube1 = Cube(4,4,4)
print(cube1.squareSquare())
print(cube1.cubeVolume())
