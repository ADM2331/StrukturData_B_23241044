                            #"pertemuan hari senin 29 April 2024"
#DENGAN MATERI
#1.inputan dari user
#2.aritmatika

#Belajar Inputan
adam = input("masukkan kata : ")
print("isi dari adam :", adam,"bertype data a;", type(adam)) #adam bertype data integer karena (bebrntuk karakter)

#Belajar Aritmatika Dasar
x = 4
y = 9


# penjumlahan 
hasil = x + y
print ("x + y =" , hasil)

#pengurangan
hasil = x - y
print ("x - y =", hasil)

#perkalian 
hasil = x * y 
print ("x * y =", hasil)

#pembagian
hasil = x / y
print ("x : y =", hasil)

#perpangkatan exponen **
hasil = x ** y
print ("x ^ y =", hasil)

#Modulus (sisa bagi / sisa dari pembagian) = %
hasil = y % x
print("x mood y =", hasil) 


#floor division (pembulatan kebawah) = //
hasil = x // y
print ("x // y =", hasil)

#Aritmatika prioritas 
#(), exponn, perkalian/pembagian, penjumlahan/pengurangan 

x = 3
y = 4
z = 5

hasil = (x ** y * (z + x) / y - z % x // y)
print(hasil)






