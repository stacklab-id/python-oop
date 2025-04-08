from module_b import greeting as greeting_module_b, Person
from module_c import greeting as greeting_module_c

if __name__ == "__main__":
    p1 = Person("taruna", 20)
    greeting_module_b(p1.name)
    greeting_module_c(p1.name)

