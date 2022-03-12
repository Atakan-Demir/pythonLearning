import json
#json dosyasını açmak için with kullanılır kapatmaya gerek yoktur
with open("users.json") as users:
    data = json.load(users) # okurken !'json.load'! kullanıyoruz

    for i in range(5):
        print("Müşteri Numarası: "+data[i]["id"])
        print("İsim Soyisim: "+data[i]["name"])
        print("Kullanıcı Adı: "+data[i]["username"])
        print("Adres Bilgisi: "+data[i]["address"]["street"]+" "+data[i]["address"]["suite"]+" "\
                 +data[i]["address"]["city"]+" "+data[i]["address"]["zipcode"])
        print("************")

