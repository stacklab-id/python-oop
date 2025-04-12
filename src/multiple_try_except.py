
try:
    result = int(input("Masukan nilai: "))
    print(10 / result)
except ValueError as e:
    print(f"tidak boleh kosong: {e}")
except ZeroDivisionError:
    print("tidak boleh dibagi dengan 0")
except Exception as e:
    print(f"terjadi kesalahan: {e}")