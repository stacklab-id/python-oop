class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} | umur: {self.age}"

s1 = Student("taruna", 20)
print(s1)