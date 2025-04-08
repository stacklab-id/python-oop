
class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

animal_1 = Cat()
animal_2 = Dog()

animal_1.eat()
animal_2.eat()