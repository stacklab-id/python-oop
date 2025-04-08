class Car:

    def __init__(self, wheel = 4):
        self.wheel = wheel
        print(f"mobil ini beroda {self.wheel}")

car1 = Car(3)
car2 = Car()

class Calculator:
    def __init__(self, *args):
        total = 0
        for value in args:
            total += value

        print(total)

cal1 = Calculator(10, 10, 10)
cal2 = Calculator(5, 5, 5)

class User:
    def __init__(self, **info):
        for key, value in info.items():
            print(f"{key}: {value}")

usr1 = User(nama = "taruna", umur = 20, gender = "laki-laki")