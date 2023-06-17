class Fraction:
    def init(self,num,denum):
            self.num = num
            self.denum = denum
    def multiply(self,t):
            temp = Fraction (1,1)
            temp.num = self.num * t.num
            temp.denum = self.denum * t.denum
            return temp
    def addition(self,term):
            temp = Fraction (1,1)
            temp.num = self.num * term.denum + term.num * self.denum
            temp.denum = self.denum * term.denum
            return temp
    def subtraction(self,subt):
            temp = Fraction (1,1)
            temp.num = self.num * subt.denum - subt.num * self.denum
            temp.denum = self.denum * subt.denum
            return temp
    def division(self, dvd):
            temp = Fraction(1,1)
            temp.num = self.num * dvd.denum 
            temp.denum = self.denum * dvd.num
            return temp
    def nod(self):
        a = self.num
        b = self.denum
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.num = self.num // (a+b)
        self.denum = self.denum // (a+b)
        return self

    def print_fraction(self):
            print('{}/{}'.format(self.num,self.denum))

r1 = Fraction(1,3)
r2 = Fraction(2,5)
r_mult = r1.multiply(r2)
r3 = r_mult.nod()
r3.print_fraction()
r4 = r_div.nod()
r4.print_fraction()
r_add = r1.addition(r2)
r_sub = r1.subtraction(r2)
r_div = r1.division(r2)
r_add.print_fraction()
r_add.print_fraction()
r_sub.print_fraction()
r_div.print_fraction()
