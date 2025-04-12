import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

def exclamation(func):
    @functools.wraps(func)
    def wrapper():
        return func() + "!"
    return wrapper

@uppercase
@exclamation
def greeting():
    return "hello python"

print(greeting())