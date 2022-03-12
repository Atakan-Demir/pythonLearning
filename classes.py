#%% Basic
# self yazmamızın sebebi bellekte class ı tutabilmek için
# self = Matematik
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2

    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2

    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2

    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2


matematik = Matematik()   # Matematik class ının bellekte yer tutup çalışabilmesini sağlıyor
matematik2 = Matematik()
print("Toplam : "+ str(matematik.topla(8,12)))



#sınıfa bağlanılır bağlanılmaz __init__ fonksiyonu yazılsada yazılmasada çalışır
class Matematik2:
    def __init__(self,sayi1,sayi2):
        self.x = sayi1
        self.y = sayi2
    def topla(self):
        return self.x + self.y

    def cikar(self):
        return self.x - self.y

    def carp(self):
        return self.x * self.y

    def bol(self):
        return self.x / self.y

mat = Matematik2(2,78)

print(mat.topla())

#%% Property (özellik)

# Sınıflar özellik tutmak için de kullanılır

class Person:
    def __init__(self,isim,soyIsim,yas):
        self.isim = isim
        self.soyIsim = soyIsim
        self.yas = yas

person1 = Person("Atakan","Demir",19)

print(person1.isim)
print(person1.soyIsim)
print(person1.yas)

class Worker(Person):  #Worker class ı Person class ından miras alacak ve özelliklerini taşıyacak
    def __init__(self,maas):
        self.maas = maas
class Customer(Person):
    def __init__(self,CreditCardNumber):
        self.CreditCardNumber = CreditCardNumber



ahmet = Worker()
mehmet = Customer()

