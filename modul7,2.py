# Fungsi untuk input data praktikan
def input_data():
    jumlah = int(input("Masukkan jumlah praktikan: "))
    data = []
    i = 0
    while i < jumlah:
        print(f"\nData Praktikan {i+1}")
        nama = input("Nama Mahasiswa      : ")
        nim = input("NIM Mahasiswa       : ")
        pretest = float(input("Nilai Pretest       : "))
        postest = float(input("Nilai Postest       : "))
        tugas = float(input("Nilai Tugas/Makalah : "))
        bonus = float(input("Nilai Bonus         : "))

        # Simpan sebagai tuple
        praktikan = (nama, nim, pretest, postest, tugas, bonus)
        data.append(praktikan)
        i += 1
    return data

# Fungsi untuk hitung nilai akhir satu orang
def hitung_nilai_akhir(pretest, postest, tugas, bonus):
    return (0.25 * pretest) + (0.25 * postest) + (0.5 * tugas) + bonus

# Fungsi untuk hitung rata-rata nilai akhir semua praktikan
def hitung_rata_rata(nilai_akhir_list):
    total = 0
    i = 0
    while i < len(nilai_akhir_list):
        total = total + nilai_akhir_list[i]
        i += 1
    return total / len(nilai_akhir_list)

# ====== Kode utama program (tanpa main) ======
data = input_data()
nilai_akhir_list = []
hasil = []

# Hitung nilai akhir per praktikan
for praktikan in data:
    nama, nim, pre, post, tugas, bonus = praktikan
    nilai_akhir = hitung_nilai_akhir(pre, post, tugas, bonus)
    nilai_akhir = min(nilai_akhir, 100)  # Batasi agar tidak melebihi 100
    nilai_akhir_list.append(nilai_akhir)
    hasil.append([nama, nim, nilai_akhir])

# Urutkan dari nilai tertinggi ke terendah
for i in range(len(hasil)):
    for j in range(i + 1, len(hasil)):
        if hasil[i][2] < hasil[j][2]:
            hasil[i], hasil[j] = hasil[j], hasil[i]

# Tambahkan peringkat
for i in range(len(hasil)):
    hasil[i].append(i + 1)

# Tampilkan hasil
print("\n{:<15} {:<10} {:<12} {:<10}".format("Nama", "NIM", "Nilai Akhir", "Peringkat"))
print("-" * 50)
for h in hasil:
    print("{:<15} {:<10} {:<12.2f} {:<10}".format(h[0], h[1], h[2], h[3]))

rata2 = hitung_rata_rata(nilai_akhir_list)
print("-" * 50)
print("{:<15} {:<10} {:<12.2f}".format("Rata-rata", "", rata2))