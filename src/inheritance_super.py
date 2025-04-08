class Animal:
    color = "orange"

    def sleep(self):
        print(f"{self.__class__.__name__} sedang tidur")

class Cat(Animal):
    def display(self):
        super().sleep()
        print(f"kucing berwarna {super().color}")

animal_1 = Cat()
animal_1.display()