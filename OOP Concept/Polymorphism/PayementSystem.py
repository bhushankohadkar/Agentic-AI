class UPIPayment:
    def pay(self, amount):
        print(f"Paid ${amount} using UPI.")

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class CashPayment:
    def pay(self, amount):
        print(f"Paid ${amount} in cash.")

payment_methods = [UPIPayment(), CreditCardPayment(), CashPayment()]

for method in payment_methods:
    method.pay(100)