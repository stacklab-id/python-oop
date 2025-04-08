class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount > self.__balance:
            print("saldo tidak cukup")
            return

        self.__balance -= amount

account = BankAccount("taruna", 2000)
print(f"saldo saat ini: {account.balance}")

account.balance = 1000

print(f"saldo saat ini: {account.balance}")
