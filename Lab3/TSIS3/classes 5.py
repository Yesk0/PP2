class account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance =  balance
    

    def deposit(self, amount):
        self.balance += amount
        print("Deposit is done")
        print("Your balance is ", self.balance)
    
    
    def withdraw(self, amount):
        if self.balance < 0 or amount > self.balance:
            print("You dont have an enough money!")
        else:
            self.balance -= amount
            print("Withdraw is done")
            print("Your balance is ", self.balance)




account1 = account("Alibek", 1000000000000000)
account1.deposit(12000000)
account1.withdraw(824320)


