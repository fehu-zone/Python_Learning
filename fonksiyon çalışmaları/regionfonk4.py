"""

hesapla() isimli fonksiyon olacak 
main kısmında 
kullanıcıdan sayı ve kaçıncı üssü alınacağı sorulur. Fonk'a paramatere olarak gönderilecek (hesapla içinde)
son kaç basamağı yazdırılacak kullanıcıdan alınır ve 
parametre olarak gelen sayıların sonucunu hesaplayıp son basamaklar yazdırılır

"""

def hesapla(taban, us):
    sonuc= taban ** us
    son = int(input("Son Kaç Basamak"))
    print(sonuc)
    print (str(sonuc) [-son:])
    

x= int(input("Taban Değerini Giriniz: "))
y= int(input( "Üs Değerini Giriniz"))

hesapla(x, y)
    