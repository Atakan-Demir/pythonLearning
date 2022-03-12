print("FAKTÖRİYEL HESAPLAMA")
print()
sayi = int(input("Hesaplanacak sayıyı giriniz : "))
faktoriyel = 1
if sayi < 0:
    print("Negatif bir sayı girdiniz!")
elif sayi == 0:
    print("Girdiğiniz sayının faktöriyeli 1 'dir.")
else:
    print("...")
    for i in range(1,sayi+1):
        faktoriyel = i * faktoriyel
        print("...")
    print("Girdiğiniz sayının faktöriyeli "+ str(faktoriyel) + " 'dir.")