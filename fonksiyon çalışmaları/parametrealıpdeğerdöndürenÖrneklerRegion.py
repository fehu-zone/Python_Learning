"""

- Birleştir() isimli iki fonksiyon yazılacak, iki parametre olacak
- kullanıcının girdiği iki ifadeyi birleştirecek,
- birleştirirken ilk harfleri büyük olarak birleştirecek 
- örn >> ali kazım
      >> Ali - Kazım

"""

"""
def birlestir(ifade1, ifade2 ):
    return "{} - {}" .format(ifade1.capitalize(), ifade2.capitalize())
     


ifade = birlestir(input("ifade1: "), input("ifade2: "))
print(ifade)

"""



















"""
- DegerGetir() isimli fonk. tanımlanacak
- kullanıcıdan iki tane kelime alacak ve bunları geri döndürecek 
- KontrolEt() isimli fonk. tanımlanacak
- diğer fonksiyondan dönen değerleri parametre olarak alacak 
, bu iki kelime arasındaki aynı olan karakterlerin sayısını ekrana yazdırır.
                örn >> ali, veli -> 2
                    >> İstanbul, İzmir -> 1 
"""



"""
def DegerGetir():
    d1= input("D1: ")
    d2= input("D2: ")
    return d1, d2 

def KontrolEt(ifade1, ifade2):
    sayac = 0 
    kontroledilen = []
    for item1 in ifade1:
        for item2 in ifade2:
            if item1 not in kontroledilen: #listede yok ise
                if item1 ==  item2:
                    kontroledilen.append(item1,)
                    sayac += 1
    print(sayac)

d1, d2 = DegerGetir()
KontrolEt(d1,d2)


"""

















"""

- 10 elemanlı dizi oluşturulur,
- Sec () isimli fonk. tanımlanır,
- Main' de kullanıcıdan sayı istenir.
- Girilen sayıyı sec() fonksiyonuna parametre olarak gönderin.
-Eger gelen sayı digit ise ve dizinin boyutundan küçükse;
- dizi içinden rastgele o kadar eleman seçilir ve yazdırılır.
- digit değilse hatalı giriş yapar

"""


def sec(p):
    if p.isdigit():
        p= int(p)
        if p<= len(dizi):
            pass
    else:
            print(" Hatalı Giriş")

dizi = [ "eleman1", "eleman2", "eleman3", "eleman4", "eleman5", "eleman6", "eleman7", "eleman8", "eleman9", "eleman10"]
sayi = input ("Sayı Giriniz: ")

sec(sayi)
sayi(sec)

#zor örnek tekrarla