
def selamVer(isim="ziyaretçi", soyisim="arkadaş"):
    print("Merhaba " + isim + " " + soyisim)


selamVer("Atakan","Demir")
selamVer("Adem")
selamVer("Hasan")
selamVer("Selma")


def selamVer(isim, soyisim="arkadaş"):
    print("Merhaba " + isim + " " + soyisim)


selamVer("Atakan","Demir")
selamVer("Adem")
selamVer("Hasan")
selamVer("Selma")


def dikUcgenAlanHesap(a,b):
    return a*b/2        #değeri geri döndürür

print(dikUcgenAlanHesap(2,5))


# Lambda (tek satır) fönksiyonlar

dikUcgenAlanHesap2 = lambda a,b : a*b/2
print(type(dikUcgenAlanHesap2))
print(dikUcgenAlanHesap2(4,5))