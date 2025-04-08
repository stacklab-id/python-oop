class BankAcount:
    def __init__(self, balance):
        self.__balance = balance

    def __get_balance(self):
        return self.__balance

    def display(self):
        return self.__get_balance()

account = BankAcount(1000)
print(account.display())