n = int(input("Jumlah data :"))
nilai = []
angka = 0

for i in range(0,n):
    j = int(input("Masukkan data ke-%d:" %(i+1)))
    nilai.append(j)
    angka += nilai[i]
    rata2 = angka / n
print("Nilai rata-rata Anda adalah %0.2f" %rata2)