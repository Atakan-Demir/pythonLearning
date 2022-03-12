
studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)  #kendi algoritmasıyla sıralar. İndex modelleme yoktur


for student in studentsSet:
    print(student)

print("Derin" in studentsSet) #True veya False değer döndürür

if "Derin" in studentsSet:
    print("Listede var")

studentsSet.add("Ali") #listeye ekleme yapar
print(studentsSet)

studentsSet.update(["Merve","Oğuz","Selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Selin") #Listeden siler (eğer listede yoksa arıza çıkarır)
print(len(studentsSet))

studentsSet.discard("Ahmet") #Listeden siler. (Arıza çıkartmaz)
print(len(studentsSet))

studentsSet.pop() # listeden rastgele eleman siler
print(studentsSet)

studentsSet.clear() #listeyi temizler ama liste kalır(boş)
print(studentsSet)

del studentsSet  #studentsSet i komple siler (destroyed)
print(studentsSet)