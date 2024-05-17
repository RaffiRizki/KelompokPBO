class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.karturencanastudi = []

    def ambil_karturencanastudi(self, karturencanastudi):
        print(self.nama + ' mengambil mata kuliah ' + karturencanastudi.nama)
        karturencanastudi.diambil_oleh(self)

class KartuRencanaStudi:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode

    def diambil_oleh(self, mahasiswa):
        print('Mata kuliah ' + self.nama + ' diambil oleh ' + mahasiswa.nama + ' (' + mahasiswa.npm + ')')

mahasiswa1 = Mahasiswa('Farel', '2255061021')
mahasiswa2 = Mahasiswa('Rahmad', '2265061002')

krs1 = KartuRencanaStudi('Pemrograman Beriorientasi Objek', 'PBO-D')
krs2 = KartuRencanaStudi('Kecerdasan Buatan', 'KB-D')

mahasiswa1.ambil_karturencanastudi(krs1)
mahasiswa2.ambil_karturencanastudi(krs2)
