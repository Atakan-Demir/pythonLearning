
sozluk = {
    "book" : "kitap",
    "table" : "masa"
}

print(sozluk["book"])
sozluk["pencil"] = "kalem"
print(sozluk["pencil"])
del sozluk["book"]
print(sozluk)

print("******")

translate = {
    "güzel" : "good",
    "bir" : "a",
    "gün":"day"
}

metin = input("bir cümle yazınız : ")

ceviri = metin.split()
print(translate[ceviri[0]])

for i in range(0,len(ceviri)):
    print(translate[ceviri[i]]+" ",end="")
