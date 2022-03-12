
sehirler = ["Ankara","İstanbul","Van","Isparta"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))


for sehir in sehirler:
    print(sehir)