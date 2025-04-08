
class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")

class Carnivora(Animal):
    def hunting(self):
        print(f"{self.__class__.__name__} sedang berburu")

class Tiger(Carnivora):
    pass

t1 = Tiger()
t1.eat()
t1.hunting()