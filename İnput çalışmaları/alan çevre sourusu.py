
"""
- pi adında değişken tanımlayın. 3. 1496546 veya 22/7
- kullanıcıdan yarıçap ve yükseklik değişkenleri alınır.
- alan = yarıçap*yükseklik*pi
yarıçapı ....., yüksekliği ...... olan koninin alanı: .....
"""


pi = 22/7
yaricap=float(input("yarıçapı gir"))
yukseklik=float(input("yükseklik gir"))
alan= yaricap * yukseklik * pi
print("yarıçapı {} olan, yüksekliği {} olan koninin alanı: {}".format(yaricap, yukseklik, alan))
