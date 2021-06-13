# Araba galerisi için mimari oluşturulacaktır
# galeride her bir arabanın marka,model, motor, yıl, renk, yaş özelliği olacak
# renk bilgisi zorunlu değildir. Girilmez ise tanımsız renk olarak ataması yapılacaktır
# aynı zamanda yaş değeri kullanıcıdan alınmayacak
# consuractor içinde hesaplama ile hesaplama yapılacaktır. 2019 yılı
# Show() fonksiyonu var. Show içinde arabanın tüm detayları düzgün biçimde formatlanarak gösterilir.


import datetime

class Araba:
    def  __init__(self, marka, model, motor, yil, renk="TANIMSIZ"):
        self.marka= marka
        self.model=model
        self.motor=motor
        self.yil=yil
        self.renk= renk
        self.yas = datetime.datetime.now().year- int(self.yil)

    def Show(self):
        return "{} {} {} {} {}".format(self.marka, self.model, self.motor, self.yil, self.renk)

a1= Araba("Audi", "TT", "2 TDI", 2018, " Kırmızı")
print(a1.Show())