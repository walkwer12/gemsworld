import hashlib
import datetime

class Block:
    def __init__(self, id, account, action, amount, balance, ph):
        self.id = id
        self.account = account
        self.action = action
        self.amount = amount
        self.balance = balance
        self.ph = ph
        self.date = datetime.datetime.now()
        self.h = self.callHash()

    def callHash(self):
        data = str(self.id) + str(self.account) + self.action + str(self.amount) + str(self.balance) + self.ph + str(self.date)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.createGBlock()]
        self.accounts = {}

    def createGBlock(self):
        return Block(1, "GENESIS", "Account Creation", 0, 0, "0")

    def addBlock(self, acc, action, amount):
        #Accoutn creation
        if action == "Acount Creation":
            if acc in self.accounts:
                print("Accoutn already exists")
                return
            self.accounts[acc] = amount

        elif action == "Deposit":
            if acc not in self.accounts:
                print("Accoutn does not exist")
                return
            self.accounts += amount

        elif action == "Withdrawal":
            if acc not in self.accounts:
                print("Accoutn does not exist")
                return

            if amount > self.accounts[acc]:
                print("Insufficient Balance")
                return
            self.accounts[acc] -= amount

        else:
            print("Invalid Transaction")
            return

        balance = self.accounts[acc]
        ph = self.chain[-1].h
        b = Block(len(self.chain), acc, action, amount, balance, ph)
        self.chain.append(b)

    def display(self):
        for b in self.chain:
            print("Block: ", b.id)
            print("Timestamp: ", b.date)
            print("Account: ", b.account)
            print("Action: ", b.action)
            print("Balance: ", b.balance)
            print("Prev hash: ", b.ph)
            print("Current Hash: ", b.h)
            print("-" * 60)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i -1]

            if current.h != current.callHash():
                return False

            if current.ph != prev.h:
                return False
        return True


p = Blockchain()

# Account Creation
p.addBlock("A101", "Account Creation", 1000)
p.addBlock("A102", "Account Creation", 500)

# Deposits
p.addBlock("A101", "Deposit", 500)
p.addBlock("A102", "Deposit", 1000)

# Withdrawals
p.addBlock("A101", "Withdrawal", 300)
p.addBlock("A102", "Withdrawal", 200)

                
