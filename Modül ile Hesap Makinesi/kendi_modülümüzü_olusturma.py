import kendi_modülüm

#print(dir(kendi_modülüm))

print("Hesap Makinesi Programı v1")

while True:
    print("Toplama için + \n çıkarma işlemi için - \n çarpma işlemi için * ")
    print(" bölme için / \n kalansız bölme için // \n üs almak için ** ")

    x= int(input("Bir Tam Sayı Giriniz:"))
    y= int(input("Bir Tam Sayı Giriniz:"))

    karar = input("Yukarıdaki Seçeneklerden Hangi İşlemi Yapacaksınız:")

    if karar == "+" :
        print("Toplama Yapılıyor")
        print("Sonuç:",kendi_modülüm.topla(x,y))
    elif karar == "-" :
        print("Çıkarma Yapılıyor")
        print("Sonuç:",kendi_modülüm.cikar(x,y))
    elif karar == "*" :
        print("Çarpma Yapılıyor")
        print("Sonuç:",kendi_modülüm.carp(x,y))
    elif karar == "//" :
        print("Kalan Bulma Yapılıyor")
        print("Sonuç:",kendi_modülüm.kalanibul(x,y))
    elif karar == "**" :
        print("Üs Alma")
        print("Sonuç:",kendi_modülüm.usal(x,y))


    karar2 = input("Çıkış için V Tuşuna Basınız")
    if karar2 == "V":
        print("İşlem Sona Ermiştir")
        break
