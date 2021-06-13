"""

degeral() isimli fonksiyon olacak
kullanıcıdan sayı alıp, bu sayının int olup olup olmadığını kontrol edecek (.isdigit komutu ile)
girilen sayı int ise sayıyı inte çevirip döndürür
değil ise -1'e döndürür
us() isimli üs alma işlemini yapacak fonksiyon olacak
degeral() fonksiyonundan dönen -1 değilse 
parametre olarak girilen değeri alır ve sayının 5. kuvvetini ekrana yazdırır
-1 ise hatalı giriş yapar 

"""

def degeral():
    sayi = input( "Lütfen Bir Sayı Girin: ")
    if sayi.isdigit:
        return int(sayi)   
    else:
       return -1

def us(taban):
    if taban == -1:
         print("Hatalı Değer ")
    else:
       print(taban*5)
       

kullanicibilgisi=degeral()
us(kullanicibilgisi)


