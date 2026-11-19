import hashlib
import datetime

class Block:
    def __init__(self, id, n, result, ph):
        self.id = id
        self.n = n
        self.ph = ph
        self.date = datetime.datetime.now()
        self.result = self.checkArmstrong()
        self.h = self.callHash()

    def callHash(self):
        data = str(self.id) + str(self.n) + str(self.ph) + str(self.date) + str(self.result)
        return hashlib.sha256(data.encode()).hexdigest()

    def checkArmstrong(self):
        num = self.n

        l = len(str(num))
        sum = 0

        while num != 0:
            digit = num % 10
            sum = sum + digit * l

            num = num // 10

        if self.n == sum:
            return "Armstrong Number"
        else:
            return "Not armstrong number"


class Blockchain:
    def __init__(self):
        self.chain = [self.createGBlock()]

    def createGBlock(self):
        return Block(1, 0, False, "0")

    def addBlock(self, n):
        ph = self.chain[-1].h
        b = Block(len(self.chain), n, False, ph)
        self.chain.append(b)

    def display(self):
        for b in self.chain:
            print(f"Block: {b.id}\nTimeStamp: {b.date}\nOriginal Number: {b.n}\nResult: {b.result}\nPrev Hash: {b.ph}\n Current Hash: {b.h}")
            print("-" * 45)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i -1]

            if current.h != current.callHash():
                return False

            if prev.h != current.ph:
                return False

        return True

p = Blockchain()

p.addBlock(9)
p.addBlock(153)
p.addBlock(3450)
p.display()

print(f"Chain Valid: {p.is_valid()}")


    

