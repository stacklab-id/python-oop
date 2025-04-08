from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow meow")

    def eat(self):
        print("nyam nyam")

class Dog(Animal):
    def speak(self):
        print("guk guk")

    def eat(self):
        print("auuuu")


