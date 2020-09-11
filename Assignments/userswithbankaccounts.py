class User: #class
    def __init__(self, name, email, accounts): #accounts is a list on creation
        self.name = name
        self.email = email
        self.accounts = {}
        for account in accounts:
            self.accounts[account] = BankAccount(int_rate=0.02, balance=0)    # added this line
    
    # adding the deposit method
    def make_deposit(self, amount, account):    # takes an argument that is the amount of the deposit
        self.accounts[account].deposit(amount)  # the specific user's account increases by the amount of the value received
        return self

    # adding the withdrawal method
    def make_withdrawal(self, amount, account):
        self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self, account):
        print("User: " + self.name + ", Balance of " + account +": $" + str(self.accounts[account].balance))
        return self

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

ethan = User("Ethan", "myemail", ["acc1", "acc2"])
print(ethan.accounts["acc1"].balance)
ethan.make_deposit(1000000000,"acc1").make_deposit(2000000000,"acc2").make_deposit(3000000000, "acc2").make_withdrawal(50, "acc1").display_user_balance("acc1").display_user_balance("acc2")

