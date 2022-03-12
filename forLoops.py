

sehirler = ["Ankara","İstanbul","İzmir","Konya"]

#print(sehirler[0])
#print(sehirler[1])
#print(sehirler[2])

for sehir in sehirler:
    print(sehir)

print("***********")

for sehir in sehirler:
    print(sehir[0:3])

print("***********")

for sehir in sehirler:
    print(sehir+" için şehir kodu = "+sehir[0:3])

print("***********")

for sehir in sehirler:
    if sehir == "İstanbul":
        break                   # döngüyü kırar ve devam etmez
    print(sehir+" için şehir kodu = "+sehir[0:3])

print("***********")

for sehir in sehirler:
    if sehir == "İstanbul":
        continue                # o anki şart için döngüyü atlar ve devam eder
    print(sehir+" için şehir kodu = "+sehir[0:3])
