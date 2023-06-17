class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def additional(self):
        return self.a + self.b
        
    def subtraction(self):
        return (self.a - self.b)
        
    def multiplication(self):
        return (self.a * self.b)
        
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ошибка (деление на 0)"
    def results_print(self):
       print(self.additional(),self.subtraction(),self.multiplication(),self.division())

math1 = Math(int(input()),int(input()))
math1.results_print()
