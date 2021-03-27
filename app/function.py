class Perusahaan:
    def __init__(self, nama, alamat, no_telepon, email):
        self.nama = nama
        self.alamat = alamat
        self.telepon = no_telepon
        self.email = email
        self.list_karyawan = []
        self.list_motor = []

    def karyawan_aktif(self, karyawan):
        self.list_karyawan.append(karyawan)

    def daftar_motor(self, motor):
        self.list_motor.append(motor)

    def total_pengeluaran(self):
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan()
        return pengeluaran

    def total_pendapatan(self):
        pendapatan = 0
        total = 0
        for karyawan in self.list_karyawan:
            pendapatan += karyawan.total_pendapatan()
        for motor in self.list_motor:
            total += motor.diskon()
        return total - pendapatan

    def total_harga_motor(self):
        total = 0
        for motor in self.list_motor:
            total += motor.diskon()
        return total

class Karyawan:
    def __init__(self, nama, pendapatan, insentif_lembur):
# NOTE: ini adalah instance variabel
        self.nama = nama
        self.pendapatan = pendapatan
        self.insentif_lembur = insentif_lembur
        self.pendapatan_tambahan = 0

# NOTE : nama instance variabel tidak boleh sama dengan nama method/fungsi,
#       jika sama akan menyebabkan error.

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

class Motor:
    def __init__(self, nama_motor, merek, harga, diskon = 0):
        self.nama_motor = nama_motor
        self.merek = merek
        self.harga = harga
        self.diskon_motor = diskon

    def diskon(self):
        total_diskon = self.harga * (self.diskon_motor/100)
        return self.harga - total_diskon

class Sales(Karyawan):
    def __init__(self, nama, pendapatan):
        super().__init__(nama, pendapatan, 0)

    # ini adalah fungsi/method untuk menghitung total uang tambahan
    # berdasarkan harga motor di kali diskon.
    def insentif_sales(self, harga_motor):
        self.pendapatan_tambahan += harga_motor * 0.01

class Teknisi(Karyawan):
    def __init__(self, nama, pendapatan, lembur = 100000):
        super().__init__(nama, pendapatan, lembur)

    # ini adalah fungsi/method untuk menghitung total uang lembur teknisi
    # berdasarkan jumlah lembur.
    def insentif_teknisi(self, jumlah_lembur = 0):
        self.pendapatan_tambahan += self.insentif_lembur * jumlah_lembur
