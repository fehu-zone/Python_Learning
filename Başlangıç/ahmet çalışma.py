musteriAdi = 'ahmet' 
musteriSoyadi = 'karadas'
musteriadsoyad = musteriAdi + ' ' + musteriSoyadi
mustericinsiyet = 'erkek'
musterikimlikno = '10000'
musteriyasi = 21
print(musteriadsoyad)
print(mustericinsiyet)
print ( musterikimlikno)

print("ahmet\nkaradaş")
print("Muhammed\t\t\tKaradaş")
print("merhaba Ahmet\'in dünyası")

print("""
Malazgirt Meydan Muharebesi, 26 Ağustos 1071 tarihinde, 
Büyük Selçuklu Hükümdarı Alparslan ile Bizans İmparatoru
IV. Romen Diyojen arasında gerçekleşen muharebedir. 
Alp Arslan'ın zaferi ile sonuçlanan Malazgirt Muharebesi
""")

a1= 5
a2= 6
a3= 67
a4= "Altındağ Mehmet Akif Ersoy Lisesi"
print(a4)

x1,x2, = 5,50 
print(x1)
 
pi=3.14
print( pi)
print( "pi değeri" + str(pi))

print( "{} pi dğerinin iki katı = {}".format(pi,(pi*2)))

#burası yorum satırı

print("yorum satırı")  #elmalı kek tarifi

#print (3) 
#print (4)

""" Objectle için str, ınt gibi şeyler yazarken yanına nokta koyarsın. objectler verilerin babasıdır"""


""" buradan itibaren string metodu başlıyor """


""" upper - BÜYÜK HARFLERE ÇEVİRİR"""

okul= "Sınav Koleji"
buyukharflerleokul= okul.upper()
print(okul)
print(buyukharflerleokul)

""" lower - küçük harflere çevirir"""

ilkokul= " NAZİFE HATUN İLKÖĞRETİM OKULU " 
print(ilkokul)
print(ilkokul.lower())

""" Title - tüm kelimelerin ilk harfi büyük""" 

ortaokul= "hayme hatun ilkokulu "
print(ortaokul)
print ( ortaokul.title())


""" capitalize - sadece ilk harf büyük diğer harfler küçük""" 

unıversıte= "bartın üniversitesi iktisadi idari bilimler fakültesi""" 

print(unıversıte)
print(unıversıte.capitalize())



""" count - kaç tane geçer/ sensiteve değildir(büyük küçük harf gözetimi yapmaz) birden çok harf/rakam okur"""


okul= "Pamukkale Üni"
print(okul)
print(okul.count("k"))




""" replace - değiştirme (title ile aynı anda kullanma oluyor mu ?)""" 
 
okul= "gülhane eğitim ve araştırma Hastahanesi"
print(okul)
print(okul.replace("gülhane eğitim ve araştırma Hastahanesi", "GATA"))

okul= "Cumhuriyet İlkokulu "
okulweb= "www.cumhuriyetilkokulu.k12.tr"
print(okul)
print(okulweb)
print(okulweb.replace("k12.tr", "meb.gov.tr"))




""" startswith - başlıyorsa true, başlamıyorsa false döndürür """

web= "www.ahmetkaradas.com"
print(web.startswith("www"))
print(web.startswith("wwa"))


""" endswith - sonu doğruysa true, değilse false döner"""

web="www.resmisite.org"
print(web.endswith("org"))
print(web.endswith("com"))

""" strip - başındaki sonundaki boşlukları alırsın..../ lstrip ise soldaki parametreleri temizler..../rsprit ise sağdaki parametreleri temizler""" 

okul= "              GOP ÜNİ.      "
print(okul.strip())

okul= ".............. BÜ ÜNİ ............"
print(okul.strip("."))

okul=".................. ANADOLU ÜNİ......"
print(okul.lstrip("."))
print(okul.rstrip("."))


""" isdigit - rakam kontrolü yapar, eğer hepsi rakamsa true, eğer hepsinde rakam yoksa false değerini döndürür"""

deger= "797884684687"
print(deger.isdigit())

deger="a797884684687"
print(deger.isdigit())

""" isalpha - harf kontrolü yapar, eğer hepsi harf ise  true, eğer hepsinde harf yoksa false değerini döndürür"""

deger= "mukavemet"
print(deger.isalpha())

deger="3pio"
print(deger.isalpha())

""" isalnum - alfanumerik kontrolü yapar(alfa numerik= a...z/0....9)"""

deger="sekizincisınıf"
print(deger.isalnum())

deger="8.sınıf"
print(deger.isalnum())

"""isupper/islower - tamamı büyük/küçük mü kontrolü yapar"""

deger= "altıncısınıf"
print(deger.islower())
print(deger.isupper())

""" isspace - tamamının space olup olmadığını kontrol eder"""

deger=("  ")
print(deger.isspace())

deger=("boşuğu     doldur")
print(deger.isspace())


""" istitle - ilk harflerin büyük olup olmadığını sorar """ 

deger= "mehmet akif Ersoy"
print(deger.istitle())

deger="Mehmet Akif Ersoy"
print(deger.istitle())

""" isdentifier - değişken ismi verilip verilmediğini kontrol eder (başta rakam olmaz,arada boşuk olmaz vb)"""

deger="1mehmetakif"
print(deger.isidentifier())

deger="mehmetakif"
print(deger.isidentifier())

deger="mehmet akif"
print(deger.isidentifier())

""" split - string bölme """
""" len komutu uzunluk verir """ 

deger= "Altındağ Mehmet Akif Ersoy Anadolu Lisesi"
print(deger.split())
print(len(deger.split()))

deger= " Mamak Sınav/Özel Kolej"
print(deger.split())
print(len(deger.split()))
print(len(deger.split("/")))

""" index - arama(hata veriyor anlamadım)"""


deger="şerife bacı mesleki ve teknik anadolu lisesi"
print(deger.index("i"))

""" format operatörü """

dil= "python"
version= "3.8.0"
print(" bu yazılım " + dil + " dilinde " + version + " versiyonunda yazılmıştır ")


""" format operatörünü (%) işareti ile kullanma """


dil="java"
version="3.7.4"
print("bu yazılım %a dilinde %a versiyonu ile yazılmıştır" % (dil,version))

""" format operatörünü ({}) işareti ile kullanma (3.2.4 yazmama rağmen neden 3.7.4 yazıyor) """


dil="c++"
versiyon= "3.2.4"
print("bu yazılım {} dilinde {} versiyonu ile yazılmıştır".format(dil,version))
print("bu yazılım {} dilinde {} versiyonu ile yazılmıştır".format(dil, version).upper())

dil="python"
us= "paytaan"
uk= "paytın"
print("{}dili Amerika aksanı ile {} şeklinde okunurken; İngiliz aksanı ile {} şeklinde okunur".format(dil,us,uk).format())

""" İç içe kullanım """

okul= "yahya kemal beyatlı ortaokulu"
print(okul)
print(okul.upper())
print(okul.upper().lower())
print(okul.upper().lower().title())
print(okul.upper().lower().title().replace("a", "q"))
print(okul.upper().lower().title().replace("a", "q").index("q"))






