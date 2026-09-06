class Accounts:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

accounts1 = Accounts("123456", "Alice", 1000)
accounts2 = Accounts("789012", "Bob", 500)
accounts3 = Accounts("345678", "Charlie", 2000)
accounts1.deposit(200)
accounts2.withdraw(100)
accounts3.withdraw(2500)  