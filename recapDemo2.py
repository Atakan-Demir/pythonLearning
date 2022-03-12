print("VERİLEN SAYI KADAR '*' YAZDIRMA")

# benim düşündüğüm

sayi = int(input("Bir sayı giriniz : "))

for x in range(1, sayi + 1):
    print("*",end="")
print()
print("////////////////////")
# hocanın yaptığı

yildiz =""

for x in range(1,sayi+1):
    yildiz = yildiz + "*"
    print(yildiz)
