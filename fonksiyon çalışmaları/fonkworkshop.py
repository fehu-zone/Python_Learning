""" -Hızlan() -Yavaşla() isimli iki fonksiyon olacak 
hızlan() >> parametre almayacak, global tanımlı hız değişkenini +5 birim değiştirecek
yavaşla()>> parametre almayacak, global tanımlı ve hız değişkenini -5 birim değiştiricek
- bilgiver() fonksiyonu olacak
anlık hızınız... km/s
- hızlan() yavaşla() fonksiyonları çağrıldığınada, ekrana aracın hız değeri yazılacak
"""









def Hizlan():
    global hiz
    global hizlimiti
    hiz += 5
    if hiz > hizlimiti:
        hiz=hizlimiti
        print(" UYARI: 120 Km/s Hızı aşamassınız!")
    print (" Anlık hızınız {} Km/s ".format(hiz))




def Yavasla():
    global hiz
    hiz -= 5
    print("Anlık hızınız {} Km/s".format(hiz))

hizlimiti=120
hiz= 110
Hizlan()
Hizlan()
Hizlan()
Hizlan()
Yavasla()
Hizlan()
Hizlan()
