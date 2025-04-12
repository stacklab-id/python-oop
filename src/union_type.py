from typing import Union

def plus(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a + b

    if isinstance(a, str) and isinstance(b, str):
        return f"{a.upper()} {b.upper()}"

    return "Tidak di izinkan"

result_str = plus("taruna", "wahyudi")
result_int = plus(20, 20)
result_false = plus(10, "20")

print(result_str)
print(result_int)
print(result_false)