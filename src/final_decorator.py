from typing import final

@final
class Person:
    pass

class Employee(Person):
    pass

class User:
    @final
    def signup(self):
        print("hello singup")

class Admin(User):
    def signup(self):
        print("from admin")