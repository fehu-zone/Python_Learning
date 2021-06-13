filmler ={

"Kara Korsanın Laneti":{"Yapım Yılı":1957,"Imdb":8.2,"Tür":"Korku"},
"Sineğin İntikamı":{"Yapım Yılı":2957,"Imdb":1.2,"Tür":"Belgesel"},


}

# Burada Liste Var

def filmEkle():
    film_adı = input ("Film Adı Girin:")
    global filmler

    yapım_yılı = input("Yapım Yılını Giriniz:")
    Imdb = input("Imdb Puanını Giriniz:")
    film_türü = input("Film Türünü Giriniz:")

    filmler[film_adı]= {"Yapım Yılı: ", yapım_yılı, "Imdb: ",Imdb,"Tür: ", film_türü}

    #filmEkle isimli fonksiyonun içine yazdığımız film_adı değerini, filmler adlı değerin içine okuttuk

    print("Film Başarıyla Eklendi")




def Filmsil():

    film_adı = input("Film adı girin: ")

    if film_adı:
        filmler.pop(film_adı)
        print("Film başarıyla silindi")
        #pop komutu komut siler 

    else:
        print("Film adı boş bırakılamaz.")


def FilmGetir():
    aranan_film_adı = input("Aradığınız Filmin Adını Giriniz:")
    if aranan_film_adı in filmler.keys():
        # in komutu = varsa
        getirilecek_film = filmler.get(aranan_film_adı)
        # Aradığımız Filmin ismini yazdık, filmler dosyasını keys komutu ile tarattık. Eğer aradığımız film ismi varsa(get komutu kullandık)
        yapım_yılı = getirilecek_film.get("Yapım Yılı:", "Yapım Yılı Girilmemiş")
        #filmEkle fonksiyonu içinde bulunan yapım_yılı komutunu çağırdık. Get komutu sayesinde eğer yapım yılı yoksa ekrana mesaj bastık 
        Imdb = getirilecek_film.get("IMBD Puanı:","IMBD Puanı Belirtilmemiş")
        film_türü = getirilecek_film.get("Film Türü: " , "Film Türü Belirtilmemiş")

        print("Film Adı: {} Yapım Yılı: {} IMBD: {} film Türü: {}".format(aranan_film_adı,yapım_yılı, Imdb, film_türü))
        print("*"*90)


def FilmleriListele():
    
    


    print ("""


    [1] Tüm Listeleri Listele
    [2] Film Arama
    [3] Film Ekleme
    [4] Film Sil


    """)




while True:


    secenek= int(input("Seçiminizi Yapınız"))

    if secenek == 1:
        filmleri_listele()
    
    elif secenek==2:
        FilmGetir()
    
    elif secenek ==3:
        filmEkle()

    elif secenek ==4:
        Filmsil()



    



  
