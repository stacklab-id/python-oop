class StackPay:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def deposit(self, jumlah_deposit):
        self.saldo += jumlah_deposit
        print("deposit berhasil")

    def tarik_tunai(self, jumlah_tarik):
        if self.saldo >= jumlah_tarik:
            self.saldo -= jumlah_tarik
            print("tarik tunai berhasil")
        else:
            print("Saldo tidak cukup")

    def cek_saldo(self):
        print(f"nama pemilik: {self.nama}")
        print(f"sisa saldo: {self.saldo}")

account = None

while True:
    print("""
        -- Selamat Datang di aplikasi StackPay --
        Silahkan pilih menu dibawah ini:
        1. Buat account
        2. Deposit
        3. Tarik
        4. Cek saldo
        5. Keluar
    """)

    menu = int(input("Pilih menu nya: "))

    match menu:
        case 1:
            if account is not None:
                print("akun sudah tersedia")
            else:
                nama = input("Masukan nama account: ")
                saldo_awal = int(input("Masukan saldo awal: "))
                account = StackPay(nama, saldo_awal)
                print("akun berhasil dibuat")
        case 2:
            if account is None:
                print("Silahkan buat account terlebih dahulu")
            else:
                jumlah_deposit = int(input("Masukan jumlah deposit: "))
                account.deposit(jumlah_deposit)
        case 3:
            if account is None:
                print("Silahkan buat account terlebih dahulu")
            else:
                jumlah_tarik = int(input("Masukan nominal tarik tunai: "))
                account.tarik_tunai(jumlah_tarik)
        case 4:
                if account is None:
                    print("Silahkan buat account terlebih dahulu")
                else:
                    account.cek_saldo()
        case 5:
            break
        case _:
            print("input yang anda masukan salah")