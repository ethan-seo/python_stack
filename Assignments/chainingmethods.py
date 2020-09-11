class User: #class
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username                    # and we use the values passed in to set the name attribute
        self.email = email_address              # and the email attribute
        self.account_balance = 0                # the account balance is set to $0, so no need for a third parameter

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    # adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

ethan = User("Ethan", "myemail")
yena = User("Yena", "myemail")
bailey = User("Bailey", "myemail")
ethan.make_deposit(1000000000).make_deposit(2000000000).make_deposit(3000000000).make_withdrawal(50).display_user_balance()
yena.make_deposit(1000).make_deposit(20000).make_withdrawal(50).make_withdrawal(100).display_user_balance()
bailey.make_deposit(1000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
ethan.transfer_money(bailey,50).display_user_balance()
bailey.display_user_balance()

