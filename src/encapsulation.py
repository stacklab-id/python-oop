class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"sisa saldo: {self.balance}")

account = BankAccount(1000)
account.display()

account.balance -= 2000
account.display()