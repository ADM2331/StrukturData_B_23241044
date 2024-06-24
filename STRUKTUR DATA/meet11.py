#Pertemuan ke 11 tgl 24 juni 2024

#tugas membuat looping

#contoh perulangan while loop
hitung= 0
while (hitung <= 5):
    print ("hitungannya adalah:", hitung )
    hitung = hitung + 1
    print ("selesai!")

#contoh perulangan for
angka = [1,2,3,4,5]
for x in angka:
    print(x)


#contoh perulangan nested 
#membuat pola bintang sgitiga
n = 5  # Jumlah baris

# Outer loop untuk mengatur jumlah baris
for i in range(1, n+1):
    # Inner loop untuk mencetak bintang pada setiap baris
    for j in range(i):
        print('*', end=' ')
    print()  # Pindah ke baris baru setelah mencetak bintang pada baris tertentu


