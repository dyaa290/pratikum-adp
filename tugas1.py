print("------------------------------SELAMAT DATANG DI RUMAH MAKAN YAYA----------------------------")
print("")
print("--------------------------------------------------------------------------------------------")
print("SILAHKAN PILIH MENU :")
print("paket A nasi goreng, es teh                                                    : Rp.30.000")
print("paket B ayam bakar, es jeruk                                                   : Rp.50.000")
print("paket C ayam saos padang, es teh                                               : Rp.40.000")
print("paket D mie rebus, es fanta susu                                               : Rp.30.000")
print("paket E mie goreng, es fanta susu                                              : Rp.30.000") 

nama_pemesan = input("masukkan nama anda      :")
nomor_pemesan = input("masukkan nomor anda     :")
alamat_pemesan = input("masukkan alamat anda    :")
print("")
print("------------------------------------------------------------------------------------------")
print("")
print(f"nama anda {nama_pemesan} dengan nomor {nomor_pemesan} dan alamat {alamat_pemesan}")
print("contoh : paket A :")
menu = input("masukkan menu           :")
if menu == "paket A" :
    harga = 30000
    nama = "paket A" 
elif menu == "paket B" :
    harga = 50000
    nama = "paket B"
elif menu == "paket C" :
    harga = 40000
    nama = "paket C"
elif menu == "paket D" :
    harga = 30000
    nama = "paket D"
elif menu == "paket E" :
    harga = 30000
    nama = "paket E"
else :
    print("menu tidak tersedia")
kuantitas = int(input("masukkan jumlah         :"))
print("")
print("------------------------------------------------------------------------------------------")
print("")
if harga > 0 :
    total = harga*kuantitas
    pajak = total*10/100
    print(f"total pesanan anda {total}")
    print(f"total pajak anda {pajak}")
    if total < 150000 :
        pengiriman = 25000
        print(f"biaya pengiriman anda {pengiriman}")
    elif total >= 150000   :
        pengiriman = 0
        print(f"gratis biaya pengiriman {pengiriman}")
    if harga > 0 :
        total_pesanan = total-pengiriman-pajak
        print(f"total pesanan {total_pesanan}")