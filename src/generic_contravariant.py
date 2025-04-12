from typing import Generic, TypeVar

T_contra = TypeVar('T_contra', contravariant=True)

class Animal:
    def __str__(self):
        return "Animal"

class Dog(Animal):
    def __str__(self):
        return "Dog"

class Trainner(Generic[T_contra]):
    def __init__(self, animal: T_contra):
        self.animal = animal

    def get_animal(self) -> None:
        print(self.animal)

def train_animal(trainer: Trainner[Dog]):
    trainer.get_animal()

trainner = Trainner[Animal](Animal())
train_animal(trainner)