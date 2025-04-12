class Connection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("creating new object")
            cls._instance = super(Connection, cls).__new__(cls)
        return cls._instance

cn1 = Connection()
cn2 = Connection()

print(cn1)
print(cn2)

print(cn1 is cn2)