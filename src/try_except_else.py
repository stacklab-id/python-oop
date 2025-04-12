
try:
    result = int(input("masukan nilai: "))
    print(10 / result)
except (ZeroDivisionError, ValueError) as e:
    print(f"Terjadi kesalahan: {e}")
else:
    print(f"tidak ada kesalahan. hasil nya: {result}")