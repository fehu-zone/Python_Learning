sayi= int(input("sayı girin: "))

for x in range (2,sayi):
    if (sayi % x) == 0:
    print("sayı asal değildir")
    break
print("bu sayı asaldır")