
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Nama: {self.name} | umur: {self.age}")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

c1 = Cat("Garfield", 20, "orange")
c1.display()