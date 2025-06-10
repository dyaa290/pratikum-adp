FILE_NAME = "data_keuangan.txt"

# Fungsi untuk memuat data dari file
def load_data():
    data = []
    file = open(FILE_NAME, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        bagian = line.strip().split(" | ")
        if len(bagian) == 4:
            entri = {}
            entri["tanggal"] = bagian[0]
            entri["keterangan"] = bagian[1]
            entri["jumlah"] = int(bagian[2])
            entri["tipe"] = bagian[3]
            data.append(entri)
    return data

# Fungsi untuk menyimpan data ke file
def save_data(data):
    file = open(FILE_NAME, "w")
    for item in data:
        baris = item["tanggal"] + " | " + item["keterangan"] + " | " + str(item["jumlah"]) + " | " + item["tipe"] + "\n"
        file.write(baris)
    file.close()

# Fungsi untuk menambahkan data keuangan
def tambah_data(data):
    print("\n== Tambah Data Keuangan ==")
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    keterangan = input("Keterangan: ")
    jumlah = input("Jumlah uang: ")
    tipe = input("Tipe (pengeluaran/pemasukan): ").lower()

    if tipe != "pengeluaran" and tipe != "pemasukan":
        print("Tipe tidak valid!")
        return

    item = {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": int(jumlah),
        "tipe": tipe
    }
    data.append(item)
    save_data(data)
    print("Data berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data
def tampilkan_data(data):
    print("\n== Data Keuangan ==")
    if len(data) == 0:
        print("Belum ada data.")
    else:
        for i in range(len(data)):
            item = data[i]
            print(str(i+1) + ". " + item["tanggal"] + " | " + item["keterangan"] + " | " + str(item["jumlah"]) + " | " + item["tipe"])
    print("=====================")

# Fungsi untuk menghapus data
def hapus_data(data):
    tampilkan_data(data)
    if len(data) == 0:
        return

    nomor = input("Masukkan nomor data yang ingin dihapus: ")
    if nomor.isdigit():
        index = int(nomor) - 1
        if index >= 0 and index < len(data):
            data.pop(index)
            save_data(data)
            print("Data berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    else:
        print("Masukkan angka yang benar.")

# Program utama
def main():
    # Buat file jika belum ada
    file = open(FILE_NAME, "a")
    file.close()

    data_keuangan = load_data()

    selesai = False
    while not selesai:
        print("\n=== MENU KEUANGAN ===")
        print("1. Tambah data keuangan")
        print("2. Hapus data keuangan")
        print("3. Tampilkan semua data")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tambah_data(data_keuangan)
        elif pilihan == "2":
            hapus_data(data_keuangan)
        elif pilihan == "3":
            tampilkan_data(data_keuangan)
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            selesai = True
        else:
            print("Pilihan tidak valid!")

main()
