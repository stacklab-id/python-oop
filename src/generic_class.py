from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content: T = content

    def get_content(self) -> T:
        return self.content

box1 = Box(100)
box2 = Box("Hello")
box3 = Box(True)

print(box1.get_content())
print(box2.get_content())
print(box3.get_content())