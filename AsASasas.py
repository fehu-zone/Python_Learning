n=1
ort=0

a = int(input("Lütfen Anne boyunu giriniz"))
b = int(input("Lütfen Baba Boyunu giriniz"))
ort = (a+b+13)/2

if ort >= 175 and ort >= 176:
    print("Çocuk Türkiye Ortalaması içinde ")
    n+=1
while n <=20:
    a = int(input("Lütfen Anne boyunu giriniz"))
    b = int(input("Lütfen Baba Boyunu giriniz"))
    ort = (a+b+13)/2
    print(ort)
    if ort >= 175 and ort >= 176:
        print("Çocuk Türkiye Ortalaması içinde ")
    else:
        print("Türkiye Sınırları Dışında")
        




