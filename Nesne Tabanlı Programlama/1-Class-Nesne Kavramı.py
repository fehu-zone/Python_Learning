"""

class ınsan:
    ad = ""
    soyad = " "

i1=ınsan()
i1.ad= "Ahmet "
i1.soyad= " Karadaş"
print(i1.ad, i1.soyad)

""" 


class ogrencı:
    AdSoyad = " "
    not1= 0
    not2= 0

o1= ogrencı()
o1.AdSoyad = input("Öğrenci Adı Ve Soyadı: ")
o1.not1 =int(input("Lütfen Öğrencinin 1. Notunu Giriniz: "))
o1.not2 =int(input("Lütfen Öğrencinin 2. Notunu Giriniz: "))
ort = (o1.not1 + o1.not2) / 2
print(ort)



"""
class ınsan:
    ad= " "
    soyad=" "

    def  __init__(self):
         self.ozellik= []


i1= ınsan()
i1.ad = "Ahmet"
i1.soyad = " Karadaş"
i1.ozellik.append("Tembel")
i1.ozellik.append("Orta Boylu")
i2= ınsan()
i2.ad= "Caner"
i2.soyad= " Yılmaz"
i2.ozellik.append("Tembel Liseli")
i3= ınsan()

print(i1.ad, i1.soyad, i1.ozellik)
print(i2.ad, i2.soyad, i2.ozellik)
print(i3.ad, i3.soyad, i3.ozellik)

"""


"""
class ogrenci:
    def  __init__(self, AdSoyad, not1,not2):
        self.AdSoyad= AdSoyad
        self.not1= not1
        self.not2= not2

    def NotHesapla(self):
        return(self.not1 + self.not2) /2


İsimSoyisim = input("Lütfen Ad Soyad Giriniz:")
n1= int(input("Lütfen N1 Giriniz:"))
n2= int(input("Lütfen N2 Giriniz:"))
o1= ogrenci(İsimSoyisim,n1,n2)
print(o1.NotHesapla())


"""

