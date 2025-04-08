class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > self.__balance:
            print("saldo tidak cukup")
            return

        self.__balance -= amount

account = BankAccount("taruna", 2000)
print(f"saldo saat ini: {account.get_balance()}")

account.set_balance(3000)

print(f"saldo saat ini: {account.get_balance()}")
