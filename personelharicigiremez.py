class Chat():
    def __init__(self, isim, soyad, mesajlar):
        self.isim = isim
        self.soyad = soyad
        self._mesajlar = mesajlar

    def getMesajlar(self):
        return "Kullanıcıya ait alt mesajlar yetkili robot tarafından sağlandı. Mesajlar: {} ".format(self._mesajlar)

    def setMesajlar(self, yeni_mesaj):
        self._mesajlar = yeni_mesaj

    def __kullanıcısil(self):
        print("Kullanıcı Silindi")

c1= Chat("faysal", "kırlangıç", " Mail Şifrem: 2425")


print(c1.getMesajlar())

c1.setMesajlar("Bu yeni mesajım")

print(c1.getMesajlar())

c1._kullanıcısil()

print(c1.__kullanıcısil)






