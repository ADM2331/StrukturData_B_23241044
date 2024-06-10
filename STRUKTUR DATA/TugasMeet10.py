                                                    #TUGAS MEET 10

MasukanRumus = input ("Penjumlahan/pengurangan : " )

if MasukanRumus == "penjumlahan1" :
    print("anda memasuki program penjumlahan")
    MasukanNilai1= int(input("Nilai :"))
    MasukanNilai2 = int(input("Nilai :"))
    nilai = (MasukanNilai1 + MasukanNilai2)
    print(nilai)
elif MasukanRumus == "pengurangan2" :
    print("anda memasuki program pengurangan2")
    MasukanNilai1= int(input("Nilai :"))
    MasukanNilai2 = int(input ("Nilai :"))
    nilai = MasukanNilai1 - MasukanNilai2
    print(nilai)
else :
    print ("Salah")