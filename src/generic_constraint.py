from typing import TypeVar

T = TypeVar('T', str, int)

def get_content(a: T, b: T) -> T:
    return a + b

print(get_content(10, 10))
print(get_content("taruna", " wahyudi"))