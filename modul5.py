list_nim = []
list_nama = []
list_nilai = []

while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nim = input("Masukkan NIM    : ")
        nama = input("Masukkan Nama   : ")
        nilai_input = input("Masukkan Nilai  : ")

        if nilai_input.isdigit():
            nilai = int(nilai_input)
        else:
            print("Nilai harus berupa angka.")
            continue

        list_nim.append(nim)
        list_nama.append(nama)
        list_nilai.append(nilai)
        print("Data ditambahkan.")

    elif pilihan == "2":
        nim = input("Masukkan NIM yang ingin dihapus: ")
        if nim in list_nim:
            i = list_nim.index(nim)
            list_nim.pop(i)
            list_nama.pop(i)
            list_nilai.pop(i)
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "3":
        if len(list_nim) == 0:
            print("Belum ada data.")
        else:
            # Bubble sort sederhana berdasarkan nilai tertinggi
            n = len(list_nilai)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if list_nilai[i] < list_nilai[j]:
                        # Tukar nilai
                        temp_nilai = list_nilai[i]
                        list_nilai[i] = list_nilai[j]
                        list_nilai[j] = temp_nilai

                        # Tukar NIM
                        temp_nim = list_nim[i]
                        list_nim[i] = list_nim[j]
                        list_nim[j] = temp_nim

                        # Tukar nama
                        temp_nama = list_nama[i]
                        list_nama[i] = list_nama[j]
                        list_nama[j] = temp_nama

            # Tampilkan data
            print("Data Mahasiswa (urut nilai tertinggi):")
            for i in range(len(list_nim)):
                print("NIM:", list_nim[i], "Nama:", list_nama[i], "Nilai:", list_nilai[i])

    elif pilihan == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid.")