""" kullanıcıdan doğum tarihi girmesi istenir 
    yaş hesaplama işlemi yapılarak, ekrana dğru formatta çıktısı verilir """

dtarihi = int(input("doğum tarihinizi girin:"))
yas= 2020 - dtarihi
print(" yaşınız : {}" .format(yas))





""" dinamik bir değer için modül atanır ( şimdilik öğrenmedik ama yine de yazacağım)"""


import datetime

dtarihi = int(input("doğum tarihinizi giriniz:"))
yas = datetime.datetime.now().year - dtarihi
print("yaşınız: {}".format(yas))
print(datetime.datetimedatetime.now().year)