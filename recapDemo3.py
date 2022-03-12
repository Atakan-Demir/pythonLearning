print("ASAL SAYI KONTROL")

sayi = int(input("Bir sayı giriniz : "))
check = True
for i in range(2,sayi):
    if sayi % i == 0:
        check = False
        break

if check == True:
    print(str(sayi) + " Asal bir sayıdır.")
else:
    print(str(sayi) + " Asal bir sayı değildir.")