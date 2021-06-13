"""

class  ınsan:
    insanlar = []

    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad 
        ınsan.ekle(self)
      
      
    @classmethod
    def ekle(cls,insannesnesi):
        ınsan.insanlar.append(insannesnesi)
        

    def __str__(self):
        return "{} {}".format(self.ad, self.soyad)

a1=ınsan("Ahmet", "Karadaş")
a2=ınsan("Samet","Güneş")
a3=ınsan("Kadir", "Çatoğlu")
a4=ınsan("Yusuf", "Şener")
a5=ınsan("Ali", "Çetindaş")

for item in ınsan.insanlar:
    print(item)

"""


class ogrenci:
    ogrencinotları = []


    def ___init__(self,ad,soyad,s1,s2):
        self.ad=ad
        self.soyad=soyad
        self.s1=s1
        self.s2=s2
        ogrenci.genelortalama(self)

    @classmethod
    def genelortalama(cls,ogrencinesnesi):
        ogrenci.ogrencinotları.append(ogrencinesnesi.nothesapla())

    def nothesapla(self):
        return(self.n1 + self.n2)/2

c1= ("Ahmet Karadaş", 30,50)
c2= ("Ali Çetindaş", 50,60)

for item in ogrenci.ogrencinotları:
    print(item)
    