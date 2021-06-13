

"""input çalışmaları yeni"""

adsoyad= input("ad soyad bilgisi giriniz:")
print(adsoyad)

sayı1 = int(input("lütfen sayı giriniz:"))
print(sayı1)
print(sayı1+5)

# kullanıcı 2 sayı girsin, ortalamasını ekrana yazdıralım

s1= int(input("sayı giriniz:  "))
s2= int(input("sayı giriniz:  "))
ortalama= (s1+s2)/2
print("{} sayısının ve {} sayısnın ortalaması {}".format(s1,s2,ortalama))


""" KULLANICIDAN S1, S2 SAYILARI ALINIR
    DÖRT İŞLEM YAPARAK, EKRANA DOĞRU FORMATTA ÇIKTISI VERİLİR
    ÇIKTI
    ..... İLE ..... SAYILARININ TOPLAMA İŞLEME SONUCU: .... 
"""

s1= int(input("sayı giriniz....:  "))
s2= int(input("sayı giriniz....:  "))
print("{} ile {} sayılarının toplama işlemi sonucu {}".format(s1,s2,(s1+s2)))

# AYNI İŞLEMİ ÇIKARMA İLE YAPALIM 
"""
s1= int(input("sayı giriniz....:  "))
s2= int(input("sayı giriniz....:  "))
print("{} ile {} sayılarının çıkarma işlemi sonucu {}".format(s1,s2,(s1-s2)))
"""

# -kullanıcıdan doğum tarihi girmesi istenir
# - yaş hesaplama işlemi yapılarak, ekrana doğru formatta çıktısı verilir

doğumtarihi= int(input("doğum tarihinizi giriniz:  "))
yas= 2020 - doğumtarihi
print("yaşınız : {}".format(yas)) 
