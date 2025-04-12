from enum import Enum, IntEnum, StrEnum

class Status(Enum):
    PENDING = 1
    ON_PROGRESS = 2
    COMPLETED = 3

class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

task = Task("Buat halaman login", Status.PENDING)

match task.status:
    case Status.PENDING: print("task ini pending")
    case Status.ON_PROGRESS: print("sedang on progress")
    case Status.COMPLETED: print("task sudah selesai")

for status in Status:
    print(f"{status.name} = {status.value}")