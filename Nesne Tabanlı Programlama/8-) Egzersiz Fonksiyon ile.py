import datetime
class Ogrenci:
    def __init__(self,ad,soyad,tc,sinif,dogumtarihi):
        self.ad=ad
        self.soyad=soyad
        self.tc=tc
        self.sinif=sinif
        self.setdogumtarihi(dogumtarihi)

    def setdogumtarihi(self,arg):
        if arg <= datetime.datetime.now().year:
            self.dogumtarihi=arg
        else:
            self.dogumtarihi = datetime.datetime.now().year



    def getdogumtarihi(self):
        return self.__dogumtarihi

    
   
    def Bilgiver(self):
        return "{} {} {} {} {} ".format(self.ad,self.soyad,self.tc,self.sinif,self.__dogumtarihi)

ogr1= Ogrenci("Adnan", "Küçükcıva", 123456,10,2009)
print(ogr1.Bilgiver())

#BU UYGULAMA DA ÇALIŞMADI