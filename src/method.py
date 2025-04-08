class Mahasiswa:
    nama = ""
    umur = 0
    jurusan = ""

    def membaca(self):
        print(f"{self.nama} sedang membaca buku")

mhs1 = Mahasiswa()
mhs1.nama = "John"
mhs1.membaca()

mhs2 = Mahasiswa()
mhs2.nama = "Doe"
mhs2.membaca()