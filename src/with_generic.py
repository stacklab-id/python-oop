from typing import TypeVar

T = TypeVar('T')

def add(a: T, b: T) -> T:
    return a + b

result_int = add(10, 10)
result_str = add("taruna", " wahyudi")

print(result_int)
print(result_str)