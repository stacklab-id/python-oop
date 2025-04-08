# class KaryawanTetap:
#     def __init__(self, nama, umur, posisi, asuransi_pensiun):
#         self.nama = nama
#         self.umur = umur
#         self.posisi = posisi
#         self.asuransi_pensiun = asuransi_pensiun
#
# class KaryawanKontrak:
#     def __init__(self, nama, umur, posisi, durasi_kontrak):
#         self.nama = nama
#         self.umur = umur
#         self.posisi = posisi
#         self.durasi_kontrak = durasi_kontrak
#
# class KaryawanLainnya:
#     def __init__(self, nama, umur, posisi, other):
#         self.nama = nama
#         self.umur = umur
#         self.posisi = posisi
#         self.other = other

class Karyawan:
    def __init__(self, nama, umur, posisi):
        self.nama = nama
        self.umur = umur
        self.posisi = posisi

    def lihat_data(self):
        print(f"""
        Nama: {self.nama}
        Umur: {self.umur}
        Posisi: {self.posisi}
        """)

class KaryawanTetap(Karyawan):
    asuransi_pensiun = ""

class KaryawanKontrak(Karyawan):
    durasi_kontrak = 0

class KaryawanOutsourcing:
    vendor = ""

karyawan_kontrak = KaryawanKontrak("taruna", 20, "Developer")
karyawan_kontrak.lihat_data()












