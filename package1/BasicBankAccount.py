class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
        def overdrawn(self):
            return self.balance < 0
        my_account = BankAccount(5000)
        my_account.withdraw(500)
        print my_account.balance