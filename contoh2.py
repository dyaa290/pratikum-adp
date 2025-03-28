baris = 6
kolom = 5
kursi_string = ""
kursi_nomor = 1
while kursi_nomor <= baris * kolom:
    kursi_string += str(kursi_nomor).rjust(2) + " "
    kursi_nomor += 1

harga_VVIP = 1000000
harga_VIP = 750000
harga_Reguler = 500000
harga_Ekonomi = 250000

def kategori_kursi(index):
    if index < 2:
        return "VVIP"
    elif index < 5:
        return "VIP"
    elif index < 15:
        return "Reguler"
    else:
        return "Ekonomi"

pesanan = ""

print("Selamat datang di sistem reservasi tiket konser!")
print("\nTampilan Layout Kursi:")
kursi_pos = 0
while kursi_pos < len(kursi_string):
    kursi_baris = ""
    kolom_count = 0
    while kolom_count < kolom * 3 and kursi_pos < len(kursi_string):
        kursi_baris += kursi_string[kursi_pos]
        kursi_pos += 1
        kolom_count += 1
    print(kursi_baris)

print("\nHarga Tiket:")
print("VVIP: Rp" + format(harga_VVIP, ','))
print("VIP: Rp" + format(harga_VIP, ','))
print("Reguler: Rp" + format(harga_Reguler, ','))
print("Ekonomi: Rp" + format(harga_Ekonomi, ','))

jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
i = 0
while i < jumlah_tiket:
    print("\nPemesanan ke-" + str(i + 1) + ":")
    nama = input("Masukkan nama Anda: ")
    nomor_kursi = input("Masukkan nomor kursi yang ingin dipesan: ")
    password = input("Buat password untuk akses konser: ")
    if " " + nomor_kursi.rjust(2) + " " in kursi_string:
        index_kursi = kursi_string.find(" " + nomor_kursi.rjust(2) + " ")
        kategori_pilihan = kategori_kursi(index_kursi // (kolom * 3))
        harga_tiket = globals()["harga_" + kategori_pilihan]
        pesanan += nama + " " + nomor_kursi + " " + kategori_pilihan + " " + str(harga_tiket) + " " + password + "\n"
        kursi_string = kursi_string.replace(" " + nomor_kursi.rjust(2) + " ", "  0 ")
        print("\n=== Struk Pemesanan Tiket ===")
        print("Nama: " + nama + "\nNomor Kursi: " + nomor_kursi + "\nKategori: " + kategori_pilihan + "\nHarga: Rp" + format(harga_tiket, ',') + "\nPassword: " + password)
        print("-------------------------")
    else:
        print("Kursi tidak tersedia atau sudah dipesan. Silakan pilih yang lain.")
    i += 1

print("\nLayout Kursi Setelah Pemesanan:")
kursi_pos = 0
while kursi_pos < len(kursi_string):
    kursi_baris = ""
    kolom_count = 0
    while kolom_count < kolom * 3 and kursi_pos < len(kursi_string):
        kursi_baris += kursi_string[kursi_pos]
        kursi_pos += 1
        kolom_count += 1
    print(kursi_baris)

print("\nTerima kasih telah melakukan reservasi!")
