"""
-User class 
    - İnit'in içinde Kullanıcı Nick'i, kullanıcı password vardır. Bunların Gelmesi Zorunlu

-Sistem Class
    - init'i içinde ad vardır. Gelmesi zorunludur.
    -login() fonksiyonuna user listesi içinden giriş yapılacak kullanıcılar gelmektedir
    kullanıcılarla beraber, klavyeden girilen ad, pw değerleri de gelecektir.
    -Eğer liste içinde bu ad, pw ye sahip kullanıcı varsa sisteme hoşgeldniz,
    yoksa hatalı giriş yapılacaktır.

"""

class user:
    kullanıcılistesi = []

    def __init__(self,nickname,password):
        self.nickname=nickname
        self.password=password
        user.ekle(self)

    @classmethod
    def ekle(cls,kl):
        cls.kullanıcılistesi.append(kl)



class sistem:
    def __init__(self,ad):
        self.ad=Ad

    def login(self,kullanıcıadı,kullanıcışifre):
        islogin=False
        for item in user.kullanıcılistesi:
            if item.nickname==kullanıcıadı and item.kullanıcışifre==password
            islogin= True
            if islogin:
                print("{} Sisteme Hoşgeldiniz {}".format(self.ad,kullanıcıadı))



            else:
                print("Hatalı Giriş Yaptınız")

u1= user("Ahmet Admin", "543")
u2= user("Mmk Admin", "321")
s1= sistem("win10")
ad=input("ad:")
pw=input("ad:")
s1.login(ad,kullanıcışifre)
for item in user.kullanıcılistesi:
    print(item.nickname,item.password)