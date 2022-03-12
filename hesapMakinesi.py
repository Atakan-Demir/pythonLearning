class Hesap:
    def __init__(self,sayi1,sayi2):
        self.x=sayi1
        self.a=sayi2
    def topla(self):
        return self.x+self.a
    def cikar(self):
        return self.x-self.a
    def carp(self):
        return self.x*self.a
    def bol(self):
        return self.x/self.a
print("Operasyon nedir ?")
print("+ : Topla")
print("- : Çıkar")
print("* : Çarp")
print("/ : Böl")
check = input("--> ")
boolean = 1
while boolean == 1:
    if check == ("+" or "-" or "*" or "/"):
        boolean = 0
    else:
        check = input("Lütfen geçerli bir operasyon seçiniz --> ")


sayi1 = int(input("1. sayıyı giriniz :"))
sayi2 = int(input("2. sayıyı giriniz :"))

hm = Hesap(sayi1,sayi2)


if check == "+":
    print(hm.topla())
elif check == "-":
    print(hm.cikar())
elif check == "*":
    print(hm.carp())
elif check == "/":
    print(hm.bol())

