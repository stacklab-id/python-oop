
def check_age(age: int):
    if age <= 0:
        raise ValueError("tidak boleh kurang dari 0")
    print("umur sudah sesuai")

try:
    check_age(0)
except ValueError as e:
    print(f"terjadi kesalahan: {e}")