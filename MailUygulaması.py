from datetime import datetime
import os, time

class EPostaServisi():
    def __init__(self,isim):
        self._isim = isim
        self._üyeler = ("Tarık","Karadaş", "ateşliboy_42", "aaa123")
        self._gönderilmiş_mailler= []

    def __str__(self):
        return self._isim + "Mail Servisine Hoşgeldiniz"
    
    def ÜyeOl(self,isim,soyad,mail,sifre):
        if self.kontrol(mail):
            print("Mail Serbest")
            Yeni_üye = isim,soyad,mail,sifre
            self._üyeler.append(Yeni_üye)
            print("Kayıt Gerçekleşti")
            input("Devam Etmek İçin Herhangi Bir Tuşa Dokunun")
        else:
            print("Bu Mail Alınmış Lütfen Başka Bir Mail Adresi Alınız ")
            print("Başka Bir Mail Almak İçin Devam Edin ( Herhangi Bir Tuşa Basabilirsiniz")

    def GirisYap(self, mail, sifre):
        if self.SifreKontrol(mail,sifre):
            print("Giriş Yapıldı. Hoşgeldiniz")
            self.KullanıcıMenüsü(self, mail)

    def KullanıcıMenüsü(self, mail):
        while True:
            os.system("cls")
            print("""
            [1] Mail Gönder
            [2] Mail Kutusuna Gönder
            [3] Çıkış Yap
            """
            )
            secim= int(input("Seçiminizi Yapınız"))

            if secim == 1:
                self.mailGönder(mail)
            elif secim == 2:
                self.mailkutusu(mail)
            elif secim == 3:
                break 

    def MailGönder(self, mail):
        alıcı = input("Alıcının Mail Adresini Giriniz")
        başlık = input("Mail Başlığını Girin")
        mesaj = input("Mesajı Giriniz")
        yeni_mail = Mail(Mail, alıcı, başlık, mesaj)
        self._gönderilmiş_mailler.append(yeni_mail)
        print("Mail Gönderildi")
        time.sleep(1)
        print("Sizi Ana Menüye Yönlendiriyorum")
        time.sleep(1)

    def MailKutusu(self,mail):
        mail_var= False
        for m in self.__gönderilmiş_mailler:
            if m.getGönderici() == mail or m.getAlıcı() == mail:
                mail_var= True
                print(m)
                if not mail_var:
                    print("Mail kutunuz boş")
                    input("Devam etmek için bir tuşa basın.")
        
        

                 

    def SifreKontrol(self, mail,sifre):
        for üye in self.__üyeler:
            kayıtlı_mail = üye[2]
            kayıtlı_Sifre = üye [3]
            if kayıtlı_mail == mail and kayıtlı_Sifre == sifre:
                return True
        return False


    def kontrol(self,mail):
    	for üye in self.__üyeler:

			kayıtlı_mail= üye[2]
			if kayıtlı_mail == mail:
				return True

            else:
                False

		


    

class Mail():
    def __init__(self, kimden, kime, başlık, mesaj):
        self.__kimden=kimden
        self.__kime = kime
        self.__başlık=başlık
        self.__mesaj= mesaj
        self.__tarih = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    	

    def getAlıcı(self):
        return self.__kime


    def getGönderici(self):
        return self.__kimden

    def __str__(self):
    		return """

		==============================================================
				
		Gönderici: {gönderici}   Alıcı: {alıcı} Tarih: {tarih}

		==============================================================

		Başlık: {konu_başlığı}

		==============================================================

		Mesaj: {mesaj}

		==============================================================

		""".format( gönderici=self.__kimden, alıcı= self.__kime, tarih=self.__tarih , konu_başlığı=self.__başlık , mesaj=self.__mesaj)




e1= EPostaServisi("Ultra MailX")

e1.ÜyeOl("Selçuk","Apar","tosbik@ultramailx.com","abc123")


            




        
 