import math

# Input jumlah titik
n = int(input("Masukkan jumlah titik: "))

# Inisialisasi array 2D untuk menyimpan koordinat
titik = []

# Mengisi array dengan koordinat dari input pengguna
for i in range(n):
    print(f"\nTitik ke-{i+1}:")
    x = float(input("  Masukkan nilai X: "))
    y = float(input("  Masukkan nilai Y: "))
    titik.append([x, y])

# Menghitung dan menampilkan jarak antar pasangan titik
print("\nJarak antar pasangan titik:")
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = titik[i]
        x2, y2 = titik[j]
        jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"  Jarak antara Titik {i+1} dan Titik {j+1}: {jarak:.2f}")