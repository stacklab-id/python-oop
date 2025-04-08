class Animal:
    color = ""

    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")

class Cat(Animal):
    def speak(self):
        print("meow meow")

c1 = Cat()
c1.color = "Orange"
c1.eat()
c1.speak()