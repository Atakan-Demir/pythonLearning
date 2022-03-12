ogrenciler = ["Atakan","Ahmet","Ali"]

#listeye(diziye) eleman ekleme
ogrenciler.append("Sultan")
print(ogrenciler)

print("********************")

#listeden(diziden) eleman çıkartma
ogrenciler.remove("Atakan")
print(ogrenciler)

print("********************")

#liste(dizi) oluşturucu (list constructor)
sehirler=list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(sehirler[1])
print(len(sehirler))

print("********************")

#Diğer fonksiyonlar
print("Ankara Sayısı = "+str(sehirler.count("Ankara")))
print("Ankara indexi = "+str(sehirler.index("Ankara")))     #en baştan başlar ve ilk bulduğunu tutar
sehirler.pop(1)     #index nunmarasına göre listeden çıkarır
sehirler.insert(0,"İstanbul")      #belilenen index numarasından eklenir
print(sehirler)
sehirler.reverse()      #listeyi tersine çevirir
print(sehirler)

print("--------------------")

sehirler3 = sehirler.copy()  #kopyalama yapar
sehirler2 = sehirler  #referans alıyor kopyalamıyor iki dizi de bellekte aynı yeri işaret ediyor
sehirler2[0]="Konya"  #referans "sehirler" olduğu için onun 0. indexini değiştirdi
print(sehirler)
print(sehirler3)

print("--------------------")

sehirler.extend(sehirler3) #"sehirler" dizisine "sehirler3" dizisini ekle
print(sehirler)

print("--------------------")

sehirler.sort()  # Alfabetik yada sayısal sıraya sokar
print(sehirler)