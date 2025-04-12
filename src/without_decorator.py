from datetime import datetime

def create():
    print("insert ke database")

def update():
    pass

def delete():
    pass

def create_with_logger():
    print(f"[{datetime.now()}] Before execute")
    create()
    print(f"[{datetime.now()}] After execute")

create_with_logger()