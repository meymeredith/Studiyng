from random import randint

class Coin:
    def __init__(self):    
        self.head = 0
        self.tail = 0

    def flip(self):
        if randint(0, 1) == 0:
            self.head += 1
        else:
            self.tail += 1

    def toss(self, count):
        for i in range(count):
            self.flip()

coin = Coin()
count = int(input())
coin.toss(count)

print("Орел " + str(coin.head) + " раз(а)")
print("Решка " + str(coin.tail) + " раз(а)")
