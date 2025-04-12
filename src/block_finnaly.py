
file = None

try:
    file = open("../data.txt", 'r')
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"file tidak ditemukan: {e}")
finally:
    if file:
        print("file ditutup")
        file.close()