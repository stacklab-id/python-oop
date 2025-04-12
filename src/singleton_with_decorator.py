from singleton_decorator import singleton

@singleton
class Connection:
    def __init__(self, host, db, username, password):
        self.host = host
        self.db = db
        self.username = username
        self.password = password

cn1 = Connection(
    host = "localhost",
    db = "belajar_python_oop",
    username = "root",
    password = "root"
)

cn2 = Connection(
    host = "10.10.10.10",
    db = "belajar_python_oop_2",
    username = "root",
    password = "root"
)

print(cn1)
print(cn2)

print(cn1 is cn2)




