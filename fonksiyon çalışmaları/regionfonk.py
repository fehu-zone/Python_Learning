"""

sonuç() isimli fonksiyon olacak 
sonuc() >> içinde s1, s2 değişkenlerine, kullanıcıdan değer alınacak
koşula göre değer dönecek

eğer s1 s2 den büyük ise çarpım değeri geriye dönecek 
eğer s1 s2 den küçük ise bölüm değeri geriye dönecek
eğer s1 s2 ye eşit ise eşitlik geriye dönecek

"""

def sonuc():
    s1= int(input("S1: "))
    s2= int(input("S2: "))
    if s1>s2:
        return s1*s2
    elif s1 == s2:
        return s1, s2
    else:
        return s1/s2
x= sonuc()
print(x)


