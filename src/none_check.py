
def say_hello(name):
    if name is None:
        print("Nama kosong")
        return
    print(f"Hello {name}")

say_hello("taruna")
say_hello(None)