import json

data = '{"firstName":"Atakan","lastName":"Demir"}' #json yapısındaki string

y = json.loads(data) # datayı json datasına dönüştürdü

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"Atakan",
    "email":"deniratakan2002@gmail.com"
}

customerJson = json.dumps(customer) # python nesnelerini json a çevirir
print(customer)

print("Atakan")
print(json.dumps("Atakan"))