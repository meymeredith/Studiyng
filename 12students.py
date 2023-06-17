class Student:
    def __init__(self,name="Ivan",groupNumber="10A",age="10"):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name

    def getGroupNumber(self):
        return self.groupNumber

    def getAge(self):
        return self.age

    def setNameAge(self,name,age):
        self.name = name
        self.age = age

    def setGroupNumber(self,groupNumber):
        self.groupNumber = groupNumber
    
student1=Student()
student1.setNameAge("Lev","22")
student1.setGroupNumber("201p")
print(student1.getName())
print(student1.getAge())
print(student1.getGroupNumber())

student2=Student()
student2.setNameAge("Lucifer","666")
student2.setGroupNumber("13H")
print(student2.getName())
print(student2.getAge())
print(student2.getGroupNumber())

student3=Student()
student3.setNameAge("Igor","21")
student3.setGroupNumber("931823")
print(student3.getName())
print(student3.getAge())
print(student3.getGroupNumber())

student4=Student()
student4.setNameAge("Anastasia","19")
student4.setGroupNumber("1B7")
print(student4.getName())
print(student4.getAge())
print(student4.getGroupNumber())

student5=Student()
student5.setNameAge("Batu","16")
student5.setGroupNumber("11C")
print(student5.getName())
print(student5.getAge())
print(student5.getGroupNumber())
