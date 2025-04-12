from typing import Protocol, runtime_checkable

@runtime_checkable
class Payment(Protocol):
    def pay(self, amount) -> None:
        ...

class CreditCard:
    def pay(self, amount) -> None:
        print("credit card")

class Paypal:
    def pay(self, amount) -> None:
        print("from paypal")

def checkout_product(payment: Payment, amount: int) -> None:
    payment.pay(amount)

obj1: Payment = CreditCard()
obj2: Payment = Paypal()

checkout_product(obj1, 1000)
checkout_product(obj2, 2000)

print(isinstance(obj1, Payment))
print(issubclass(CreditCard, Payment))





