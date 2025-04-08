
class Omnivora:
    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")

class Carnivora:
    def hunting(self):
        print(f"{self.__class__.__name__} sedang berburu")

class Beruang(Omnivora, Carnivora):
    pass

beruang_1 = Beruang()
beruang_1.hunting()
beruang_1.eat()

