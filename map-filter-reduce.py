###mapping
sayilar = [1,2,3,4,5]

sayilarKareleri = list(map(lambda sayi:sayi**2,sayilar))

#sayilarKareleri = []
#for sayi in sayilar:
#    sayilarKareleri.append(sayi*sayi)

print(sayilarKareleri)
###filter
sayilarFiltreli = list(filter(lambda sayi:sayi>2,sayilar))
print(sayilarFiltreli)

### reduce
from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)
#ilk işlem için x=1 y=2 sonuc=2, artık ikinci islem için x=2 y=3
#sonuc=6, şimdi üçüncü islem için x=6 y=4 .......
print(sayilarFaktoriyel)