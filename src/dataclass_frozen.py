from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p1: Person = Person("Taruna", 20)
p2: Person = Person("Taruna", 20)
print(p1)

print(p1)