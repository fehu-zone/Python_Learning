class urun:
    def__init__(self,urunıd,ad,birimfiyat,birimbasinamiktar,kdv):
       self.urunıd=urunıd
       self.ad=ad
       self.birimfiyat=birimfiyat
       self.birimbasinamiktar=birimbasinamiktar
       self.kdv=kdv
      


 class sepeturunu:
     def __init__(self,urun,adet):
         self.urun = urun
         self.adet = adet
     
     
     def sepeturunu(self):
         if self.urun.birimbasinamiktar=="TL,Kg":
             return round(self.urun.birimfiyati *self.adet,2)
         elif self.urun.birimbasinamiktar == "GR.PKT":
             return round(self.urun.birimfiyati * self.adet/1000,2)




class sepet:
    def__init__(self,musteriıd, surunler):
       self.musteriıd=musteriıd
       self.surunler=surunler

    def kdv(self):
        toplamkdv=0
        for item in self.surunler:
            if item.urun.birimbasinamiktar == "TL/Kg.": 
                toplamkdv += item.urun.birimfiyati * item.adet * item.urun.kdv
            elif item.urun.birimbasinamiktar == "GR.PKT":
        return round(toplamkdv,2)


    def bilgiver(self):
        for item in self.urunler:
            print("""
                     {} {} {}   {} {} {}"""
                    .format(item.urun.ad,
                            str(item.adet),
                            str(item.urun.birimbasinamiktar),
                            str(item.urun.birimfiyati),
                            str(item.urun.kdv),
                            str(item.urunfiyati())))

        print("""
                    {}""".format("-"*40))

        print("""
         TOPkdv                     :  {}
        """.format(self.kdv()))
        



#region
u1=urun(1,"Çay", 5,95, "TL,Kg.", 0.08)
u2=urun(1,"Kahve", 8.99, "TL/Kg.",0.08)
u3=urun(1,"Mantar", 4,85, "GR.PKT", 0.08)
#endregion


sepeturunleri= [sepeturunu(u1,1), sepeturunu(u2,2), sepeturunu(u3,400)]
   
s= sepet("Aziz", sepeturunleri)