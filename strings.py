# -*- coding: utf-8 -*-
# substring
mesaj = "Merhaba dünya"
print(mesaj[2:5])
yeniMesaj = mesaj[12:13]
print(yeniMesaj)

# len
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

# lower upper
print(mesaj.upper())
print(mesaj.lower())

# replace
# mesaj = mesaj.replace("ü","u")
print(mesaj.replace("ü","u"))
print(mesaj)
print(mesaj.replace("a","e"))

# split ve strip
bilgi = "     Engin;Demiroğ;33;Ankara ".strip()
print(bilgi.split())
print("Adı = " + bilgi.split(";")[0])

# input
ad = input("Adınız?")
sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ")
print(int(sayi1) + int(sayi2))



