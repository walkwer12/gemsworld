import hashlib
import datetime

class Block:
    def __init__(self, id, arr, ph):
        self.id = id
        self.arr = arr
        self.ph = ph
        self.date = datetime.datetime.now()
        self.result = self.checkAnagram()
        self.h = self.callHash()

    def callHash(self):
        data = str(self.id) + str(self.arr) + str(self.date) + self.ph + str(self.result)
        return hashlib.sha256(data.encode()).hexdigest()

    def checkAnagram(self):

        #two words in the array
        w1 = self.arr[0]
        w2 = self.arr[1]

        #replace spaces with no spaces and lower the words
        w1 = w1.replace(" ", "").lower()
        w2 = w2.replace(" ", "").lower()

        if sorted(w1) == sorted(w2):
            return True
        else:
            return False

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(1, [" ", " "], "0")

    def addBlock(self, w1, w2):
        ph = self.chain[-1].h
        b = Block(len(self.chain), [w1, w2], ph)
        self.chain.append(b)

    def display(self):
        for b in self.chain:
            print(f"Block ID: {b.id}\nTimestamp: {b.date}\nWord 1: {b.arr[0]}\nWord 2: {b.arr[1]}\nResult: {b.result}")
            print(f"Current hash: {b.h}\nPrev Hash: {b.ph}")
            print("="*60)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]

            if current.h != current.callHash():
                return False

            if current.ph != prev.h:
                return False

        return True

p = Blockchain()

p.addBlock("silent", "listen")
p.addBlock("White", "black")

p.display()

print(f"Valid Chain: {p.is_valid()}")

