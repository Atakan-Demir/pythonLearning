#Setlerde iki aynı data olamaz hata verir.
#iki farklı seti çakışmadan kesiştirmek için bu yöntemler kullanılır

setA={1,2,3,4}
setB={3,4,5,6}

#Birleşim kümeleri
print("--------------")
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))
print("--------------")

#Kesişim kümeleri
print("--------------")
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))
print("--------------")

#Fark kümeleri
print("--------------")
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))
print("--------------")

#Farkların birleşim kümesi
print("--------------")
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
print("--------------")