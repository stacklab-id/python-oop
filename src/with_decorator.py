import functools
from datetime import datetime

def log(func):
    @functools.wraps(func)
    def wrapper():
        print(f"[INFO - {datetime.now()}] before execute")
        func()
        print(f"[INFO - {datetime.now()}] after execute")

    return wrapper

@log
def create():
    """melakukan insert ke database"""
    print("insert database")

@log
def update():
    print("update database")

@log
def delete():
    print("delete database")

create()
update()
delete()

print(create.__name__)
print(create.__doc__)