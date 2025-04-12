from typing import TypeVar, Generic

class Animal:
    pass

class Dog(Animal):
    pass

T_co = TypeVar('T_co', covariant=True)

class Trainner(Generic[T_co]):
    def __init__(self, animal: T_co):
        self.animal = animal

    def get_animal(self) -> T_co:
        return self.animal

t1: Trainner[Animal] = Trainner(Dog())
print(type(t1.get_animal()))










