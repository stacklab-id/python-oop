
try:
    result = int(input("masukan nilai: "))
    print(10 / result)
except (ValueError, ZeroDivisionError) as e:
    print(f"terjadi kesalahan: {e}")
