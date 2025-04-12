class Person:
    def __init__(self, name: str, age: int, is_active: bool) -> None:
        self.name: str = name
        self.age: int = age
        self.is_active: bool = is_active

    def __repr__(self):
        return f"name: {self.name} | umur: {self.age} | active? {self.is_active}"

person: Person = Person("taruna", 20, True)
print(person)