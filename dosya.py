
#r (read)Okuma, a (append)Ekleme, w (write)Yazma, x (create)Oluşturma

f = open("musteriler.txt","r") #Dosyayı okumak için açar

#print(f.read()) # dosyayı okur

print("********")

print(f.readline()) # dosyayı satır satır okur

for i in f:
    print(i,end="")

f.close()  # dosyayı kapatır


fileToAppend = open("ogrenciler.txt","a") # eğer a -> w olursa varolan dosyanın üzerine yazar ve veri kaybı olabilir
fileToAppend.write("\n") #enter basarak yarması demek
fileToAppend.write("Atakan")
fileToAppend.close()

import os

if os.path.exists("ogrenciler.txt"): #sistemde olup olmadığını kontrol eder.
    os.remove("ogrenciler.txt") # dosyayı siler
else:
    print("dosya yok")

os.rmdir("dosya") # ismi verilen klasörü siler
