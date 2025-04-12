class Product:
    def __init__(self, name: str, price: float, qty: int) -> None:
        self.name: str = name
        self.price: float = price
        self.qty: int = qty

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, qty={self.qty})"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price

product_1 = Product("iPhone 15 Pro Max", 10.000000, 10)
product_2 = Product("iPhone 15 Pro Max", 10.000000, 20)

print(product_1)

print(product_1 == product_2)