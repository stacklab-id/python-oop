class Animal:
    def speak(self):
        print("speak from animal")

class Cat(Animal):
    def speak(self):
        print("speak from cat")

c1 = Cat()
c1.speak()