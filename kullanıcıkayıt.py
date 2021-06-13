def Kayıt_ol():
    kullanıcı_adı = input("Kullanıcı Adı Giriniz: ")
    if kullanıcı_adı in open("kullanıcılar.text", "r").read():
        return Kayıt_ol()
    dosya.write(kullanıcı_adı)
    dosya.write(" ")
    sifre = input("Şifrenizi Giriniz")
    dosya.write(sifre)
    dosya.write("\n")
    sifre_yeniden = input("Şifrenizi Tekrar Giriniz")

    if sifre != sifre_yeniden:
        print("======== ŞİFRELER EŞLEŞMEDİ ============" )
        return Kayıt_ol()

dosya=open("kullanıcılar.text","w")
dosya.write("kullanıcı_adı")
dosya.write(" ")
dosya.write("sifre")
dosya.write(" ")
print("Kullanıcı Kaydedildi")

Kayıt_ol()
dosya.close()
