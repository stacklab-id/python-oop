from typing import TypeVar

class Person:
    pass

class Student(Person):
    pass

class Other:
    pass

T = TypeVar('T', bound=Person)

def get_value(obj: T) -> None:
    print(type(obj))

get_value(Person())
get_value(Student())
get_value(Other())