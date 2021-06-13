import time
import random

print("SAYI TAHMİN OYUNUNA HOŞGELDİNİZ")
print("1 İle 10 arasında sayı tahmin ediniz")
rastgele_sayi = random.randint(1,10)
tahmin_hakki = 5

while True:

    tahmin = int(input("Tahmininiz:"))

    if tahmin == rastgele_sayi:
        time.sleep(3)
        print("Tebrikler Tahmininiz Doğru")
        print("Rastgele sayı", rastgele_sayi)
    elif tahmin != rastgele_sayi:
        print("Tahmininiz yanlış")
        tahmin_hakki -=1

    if tahmin_hakki == 0 :
        print("Deneme Hakkınız Bitti ")
        print("Doğru Rastgele Sayı", rastgele_sayi)
        break

    else:
        time.sleep(3)
        print("Bir tahmin hakkı daha veriyoruz")
        tahmin_hakkı =1
