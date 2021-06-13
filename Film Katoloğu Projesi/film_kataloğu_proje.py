filmler ={

"Kara Korsanın Laneti":{"Yapım Yılı":1957,"Imdb":8.2,"Tür":"Korku"},
"Sineğin İntikamı":{"Yapım Yılı":2957,"Imdb":1.2,"Tür":"Belgesel"}


}



def filmEkle():
    film_adı = input ("Film Adı Girin:")
    global filmler

    if film_adı:
        yapım_yılı = input("Yapım Yılını Giriniz:")
        Imdb = input("Imdb Puanını Giriniz:")
        film_türü = input("Film Türünü Giriniz:")

        filmler[film_adı]= {"Yapım Yılı": yapım_yılı, "Imdb":Imdb,"Tür":film_türü}

        print("Film Başarıyla Eklendi")
    else:
        print("Film Adı Boş bırakılamaz")




def Filmsil():

    film_adı = input("Film adı girin: ")

	if film_adı:
		filmler.pop(film_adı)
		print("Film başarıyla silindi")

	else:
		print("Film adı boş bırakılamaz.")





while True:

    print ("""

        [1] Tüm Filmleri Listele
        [2] Film Arama
        [3] Film Ekle
        [4] Film Sil


          """)


secenek= int(input("Seçiminizi Yapınız"))
if secenek == 1:
    filmleri_listele()
elif secenek==2:
    film_getir()
elif secenek ==3:
    filmEkle()
elif secenek ==4:
    Filmsil()
