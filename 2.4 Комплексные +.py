class integer: 
    @staticmethod
    def summ(x,y): 
        return x + y
    @staticmethod
    def subb(x,y): 
        return x - y
    @staticmethod
    def mull(x,y): 
        return x * y
    @staticmethod
    def divv(x,y): 
        return x / y
class complexnum(integer): 
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def summ(self,second): 
        x=integer.summ(self.a,second.a)
        y=integer.summ(self.b,second.b)
        print("%d + i %d" %(x,y))
    def subb(self,second): 
        x=integer.subb(self.a,second.a)
        y=integer.subb(self.b,second.b)
        print("%d + i %d" %(x,y))
    def mull(self,second): 
        x=integer.subb(integer.mull(self.a,second.a),integer.mull(self.b,second.b))
        y=integer.summ(integer.mull(self.a,second.b),integer.mull(self.b,second.a))
        print("%d + i %d" %(x,y))
    def divv(self,second):
        num1=integer.summ(integer.mull(self.a,second.a),integer.mull(self.b,second.b))
        den=integer.summ(integer.mull(second.a,second.a),integer.mull(second.b,second.b))
        num2=integer.subb(integer.mull(second.a,self.b),integer.mull(self.a,second.b))
        x=integer.divv(num1,den)
        y=integer.divv(num2,den)
        print("%f + i %f" %(x,y))
c1=complexnum(12,13)
c2=complexnum(14,15)
c1.summ(c2)
c1.subb(c2)
c1.mull(c2)
c1.divv(c2)
