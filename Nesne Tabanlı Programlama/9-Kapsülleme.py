class ogrenci:
 def __init__(self,ad,soyad,tc,sinif, okul):   
    self.ad=ad 
    self.soyad=soyad
    self.tc=tc 
    self.setsinif(sinif)
    self.setokul(okul)

 def setokul(self,arg):
     if arg != "AMAEAL":
         self.okul= -1
     else:
         self.okul = -1 
 def getokul(self):
     return self.__okul


 def setsinif(self,arg):
     if 8 < arg< 13:
         self.__sinif = arg
     else:
         self.__sinif = -1

 def bilgiver(self):
     if self.getsinif()==-1:
         return "Üzgünüz!! Sınıf Seviyesi uygun değil 9-12 dışındak ayıt kabul edilemez"
     if self.getokul()== -1:
         return " Amaeal Dışı Kayıt Alamayız"  
     return " {} {} {} {}".format(self.ad,self.soyad,self.tc,self.__sinif, self__okul)


ogr1=ogrenci("Ahmet","Mehmet",12345, "9", "At Lisesi")
print(ogr1.bilgiver())

#UYGULAMA ÇALIŞMADI TEKRAR YAZILACAK 