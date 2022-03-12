tupleListe=(2,4,6,"Ankara",(2,3,4),[])
liste=[2,4,6,"Ankara",[3,4,5],()]
print(type(tupleListe))
print(type(liste))
print("-----------------")
print(tupleListe)
print(liste)
print("-----------------")
print(len(tupleListe))
print(len(liste))
print("-----------------")
liste[0]="6"
#tupleListe[0]="6"   //* buna izin verilmez çünkü tuple tipi dizinin verileri sabittir.
                    #  readonly olarak bellleğe alındığı için daha verimlidir.

print(tupleListe[-2])   # sağdan 2. denektir
print(liste[-2])

print("-----------------")

print(tupleListe[1:2])
print(liste[1:2])

print("-----------------")

tupleDeger = ("Atakan",) # Eğer tek eleman varsa veri tipinin tuple olduğunu sisteme
print(type(tupleDeger))  # söylemek için "," (virgül) koyulur.
