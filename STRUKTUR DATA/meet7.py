                        #PERTEMUAN KE 7 Tgl 13 Mei 2024
#TABEL KEBENARAN (LOGIKA BOLEAN)
#NOT and or xor

#not
print("-----Logika Not-----")
x = False
y = not x
print('value x =' ,x)
print('-----------NOT')
print('value y =' ,y)

#OR (semua bernilai True selama ada True) #berlaku untuk perempuan (karena selalu benar)
print("-----Logika And-----")
x = False
y = False
z = x or y
print(x,'OR', y, 'adalah', z)

print("-----Logika OR-----")
x = False
y = True
z = x or y
print(x,'OR', y, 'adalah', z)

print("-----Logika OR-----")
x = True
y = False
z = x or y
print(x,'OR', y, 'adalah', z)

print("-----Logika OR-----")
x = True
y = True
z = x or y
print(x,'OR', y, 'adalah', z)

#And (hanya bernilai True, ketika keduanya True) #berlaku untuk lelaki (karena selalu salah)
print("-----Logika And-----")
x = False
y = False
z = x and y
print(x,'And', y, 'adalah', z)

print("-----Logika And-----")
x = False
y = True
z = x and y
print(x,'And', y, 'adalah', z)

print("-----Logika And-----")
x = True
y = False
z = x and y
print(x,'And', y, 'adalah', z)

print("-----Logika And-----")
x = True
y = True
z = x and y
print(x,'And', y, 'adalah', z)


#XOR (dengan lambang = ^ ) 
#(jika keduanya sama, hasilny False, sisanya berarti True)
print("-----Logika XOR-----")
x = False
y = False
z = x ^ y
print(x,'XOR', y, 'adalah', z)

print("-----Logika XOR-----")
x = False
y = True
z = x ^ y
print(x,'XOR', y, 'adalah', z)

print("-----Logika XOR-----")
x = True
y = False
z = x ^ y
print(x,'XOR', y, 'adalah', z)

print("-----Logika XOR-----")
x = True
y = True
z = x ^ y
print(x,'XOR', y, 'adalah', z)
