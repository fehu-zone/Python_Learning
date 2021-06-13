"""


def Topla(x,y, sonuç="TOTAL:"):
    print(sonuç, x+y)

Topla(8, 9)

     """





"""
def Kayitol(Tc, ad= "Anonim ", Soyad= "Anonim", Mail= "@"):
    print("Kaydınız Başarı İle Oluşturuldu")
    print(Tc, ad, Soyad,  Mail)

Kayitol=(6589657412, "Ahmet", "Karadaş", "ahmettkara94@gmail.com")

#bu uygulamayı çalıştıramadım

"""








#region opsiyonel olarak
'''

- start(ad) ->fonk. yazılacak parametresi olacak
- parametre girilmek zorunda olmayacak. Girildiğinde/Girilmediğinde?;
-Karakter adı varsa o isimle giriş yapılır 
- yoksa name216534
- 1-1000 arasında rastgele sayı verilir

'''



import random

def start(ad="Anonim" + str(random.randint(1, 9876))):
    print("Hoşgelndiz", ad)

start()