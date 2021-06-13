# Calisan class
# BilgiVer() -> kullanıcının bilgileri yazdırılır
# ZamYap(tl) -> eğer yapılmak istenen zam miktarı maaşın yarısından fazlaysa "emin misin?"  diye sorulur
# Cevap e ise zam yapılır değil ise H ise bir şey yapılmaz

# Şirket Class
# AlimYap() -> çalışan sınıfından nesneyi gönderip bilgilerini yazıp, işe yapılır.
# Istencıkar() -> çalışan sınıfından nesneyi gönderip bilgilerini, işten çıkarılır
#bu uygulama istediğim gibi olmadı yeniden deneyeceğim

class Calisan:
    def __init__(self,ad,soyad,maas,tc):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.tc=tc
    def ZamYap(self,miktar):
        if miktar>= self.maas/2:
            soru= input("Girilen Miktar, Maaşınızın %50'sinden fazla mı?")
print("Zam yapıldı, Yeni maaş miktarı {}".format(.self.maas))

        else:

        self.maas += miktar
print("zam yapıldı, Yeni maaş miktarı {}".format(self.maas))





    def BilgiVer(self):
        return "{} {} {} {}".format(self.ad,self.soyad,self.maas,self.tc)


A1= Calisan("Ahmet", "Karadaş", 12000, "41541645113")
print(A1.BigiVer())
