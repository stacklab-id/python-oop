import json, hashlib

class Helper:
    class Converter:
        @staticmethod
        def dict_to_json(value):
            return json.dumps(value, indent=4)

    class Hash:
        @staticmethod
        def sha256(value):
            object_hash = hashlib.sha256()
            hashed = object_hash.update(value.encode('utf-8'))
            return object_hash.hexdigest()

dict = {
    "name" : "taruna",
    "age" : 20,
    "posisiton" : "developer"
}

response_json = Helper.Converter.dict_to_json(dict)
print(response_json)

password = Helper.Hash.sha256("admin123")
print(password)