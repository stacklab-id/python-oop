class Connection:
    __instance = None

    @staticmethod
    def create_instance():
        if Connection.__instance is None:
            Connection()
        return Connection.__instance

    def __init__(self):
        if Connection.__instance is not None:
            raise "object sudah pernah dibuat"
        else:
            Connection.__instance = self

cn1 = Connection.create_instance()
cn2 = Connection.create_instance()

print(cn1)
print(cn2)

print(cn1 is cn2)