from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1: Person = Person("Taruna", 20)
p2: Person = Person("Taruna", 20)
print(p1)

print(p1 == p2)