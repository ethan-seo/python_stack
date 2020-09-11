class BankAccount: 
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.balance = balance

    # adding the deposit method
    def deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.balance += amount	# the specific user's account increases by the amount of the value received
        return self

    # adding the withdrawal method
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

ethan = BankAccount(.01, 1000000)
yena = BankAccount(.01, 1000)
ethan.deposit(1000000000).deposit(2000000000).deposit(3000000000).withdraw(50).yield_interest().display_account_info()
yena.deposit(1000).deposit(20000).withdraw(50).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

