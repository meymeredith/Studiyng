class ATM:
    def __init__(self):
        self.balance = 0;
    
    def dep(self, sum):
        self.balance += sum

    def sn(self, sum):
        if self.balance < sum:
            print("Balance Error")
        else:
            self.balance -= sum

    def check(self):
        print(str(self.balance) + "р.")


atm = ATM()
atm.check()
atm.dep(100)
atm.check()
atm.sn(46)
atm.check()
atm.sn(55)
