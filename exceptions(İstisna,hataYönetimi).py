
try: # dene hata alırsan
    sayi = int(input("Bir sayı giriniz: "))
except ValueError:
    print("Tip Uyuşmazlığı: Lütfen sadece sayı giriniz.")
except ZeroDivisionError:
    print("Payda sıfır olamaz!")
except: #bunu yap
    print("Bir hata oluştu")
finally:
    print("Bitti") # herdurumda çalışacak

