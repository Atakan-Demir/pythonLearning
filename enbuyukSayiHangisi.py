
sayi1=int(input("Sayı giriniz: "))
sayi2=int(input("Sayı giriniz: "))
sayi3=int(input("Sayı giriniz: "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    print("en büyük sayı "+str(sayi1)+" dir.")
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    print("en büyük sayı "+str(sayi2)+" dir.")
elif (sayi3 >= sayi2) and (sayi3 >= sayi1):
    print("en büyük sayı "+str(sayi3)+" dir.")