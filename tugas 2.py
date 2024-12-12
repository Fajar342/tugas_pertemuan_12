class DaftarNilaiMahasiswa:
    def _init_(self):
        # Inisialisasi data sebagai list kosong di constructor
        self.data = []

    def tambah(self):
        nama = input("Masukkan nama mahasiswa: ")
        nilai = input(f"Masukkan nilai untuk {nama}: ")
        self.data.append({"nama": nama, "nilai": nilai})
        print(f"Data {nama} berhasil ditambahkan.\n")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.\n")
            return
        print("Daftar Nilai Mahasiswa:")
        for mahasiswa in self.data:
            print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
        print()  # New line

    def hapus(self, nama):
        ditemukan = False
        for mahasiswa in self.data:
            if mahasiswa['nama'] == nama:
                self.data.remove(mahasiswa)
                print(f"Data {nama} berhasil dihapus.\n")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Data {nama} tidak ditemukan.\n")

    def ubah(self, nama):
        ditemukan = False
        for mahasiswa in self.data:
            if mahasiswa['nama'] == nama:
                nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
                mahasiswa['nilai'] = nilai_baru
                print(f"Nilai {nama} berhasil diubah.\n")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Data {nama} tidak ditemukan.\n")


# Contoh penggunaan
daftar_nilai = DaftarNilaiMahasiswa()

while True:
    print("Menu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Ubah data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        daftar_nilai.tambah()
    elif pilihan == "2":
        daftar_nilai.tampilkan()
    elif pilihan == "3":
        nama_hapus = input("Masukkan nama yang akan dihapus: ")
        daftar_nilai.hapus(nama_hapus)
    elif pilihan == "4":
        nama_ubah = input("Masukkan nama yang akan diubah: ")
        daftar_nilai.ubah(nama_ubah)
    elif pilihan == "5":
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")
