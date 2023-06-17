class Car():
    def __init__(self,color="Нет",type="Нет",year="Нет"):
        self.color = color
        self.type = type
        self.year = year

    def carStart(self):
        print ("Автомобиль заведён")

    def carStop(self):
        print ("Автомобиль заглушён")

    def setColor(self,color):
        self.color = color

    def setType(self,type):
        self.type = type

    def setYear(self,year):
        self.year = year

    def carShow(self):
        print('{},{},{}'.format(self.color,self.type,self.year))

car1 = Car()
car1.setColor("Розовый")
car1.setType("Внедорожник")
car1.setYear("2021")
car1.carShow()
car1.carStart()
car1.carStop()