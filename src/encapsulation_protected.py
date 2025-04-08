class BankAcount:
    def __init__(self, balance):
        self._balance = balance

    def _get_balance(self):
        return self._balance

    def display(self):
        return self._get_balance()

account = BankAcount(1000)
print(account.display())
print(account._balance)