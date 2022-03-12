
ogrenciler = ["Atakan","Salih","Derin","Hasan","Sultan","Aysun"]

fileToAppend = open("ogrenciler.txt","a") #eklemek için aç yoksa oluştur

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close() # dosyayı kapat