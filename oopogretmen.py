class Ogretmenler():
    def __init__(self, isim, soyad, id, maas):
        self.isim = isim
        self.soyad = soyad
        self.id = id
        self.maas = maas

    
    def Kimliksorgula(self):

        print("Numara: {}  |  Adı: {} | Soyadı: {} | Maas: {} |".format(self.id, self.isim, self.soyad, self.maas))


class Kimya_Ogretmenleri(Ogretmenler):
    def __init__(self, isim, soyad, id, maas, labsuresi):
        super().__init__(isim,soyad, id, maas)
        self.labsuresi = labsuresi


    def Kimliksorgula(self):
        super().Kimliksorgula()
        print("Ben Kimya Öğretmeniyim")




k1= Kimya_Ogretmenleri("Salih", "Güney", 45643215, 4200, 15)
k1.Kimliksorgula()


#Lab süresini ekrana yazdıramadım

