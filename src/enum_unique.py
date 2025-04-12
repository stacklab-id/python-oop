from enum import Enum, unique

@unique
class Numbers(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

for number in Numbers:
    print(f"{number.name} = {number.value}")