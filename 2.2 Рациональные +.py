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
class complex(integer): 
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def summ(self,num): 
        x=integer.summ(self.a,num.a)
        y=integer.summ(self.b,num.b)
        print("%d + i %d" %(x,y))
    def subb(self,num): 
        x=integer.subb(self.a,num.a)
        y=integer.subb(self.b,num.b)
        print("%d + i %d" %(x,y))
    def mull(self,num): 
        x=integer.subb(integer.mull(self.a,num.a),integer.mull(self.b,num.b))
        y=integer.summ(integer.mull(self.a,num.b),integer.mull(self.b,num.a))
        print("%d + i %d" %(x,y))
    def divv(self,num):
        num1=integer.summ(integer.mull(self.a,num.a),integer.mull(self.b,num.b))
        den=integer.summ(integer.mull(num.a,num.a),integer.mull(num.b,num.b))
        num2=integer.subb(integer.mull(num.a,self.b),integer.mull(self.a,num.b))
        x=integer.divv(num1,den)
        y=integer.divv(num2,den)
        print("%f + i %f" %(x,y))
c1=complex(1,6)
c2=complex(5,7)
c1.summ(c2)
c1.subb(c2)
c1.mull(c2)
c1.divv(c2)