def add(x: int, y: int) -> int:
    return x + y

result: int = add(10, 20)
print(result)
print(type(result))

def say_hello(name: str) -> None:
    print(f"hai {name}")

say_hello("taruna")