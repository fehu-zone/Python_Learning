""" kullanıcıdan denklemin katsayı, sabit değer bilgileri alınır, a-b
kök = -b/a
              çıktı
              1. dereceden katsayısı {} olan ve sabit değeri {} olan denklemin kökü 
"""

a= int(input("a katsayısını giriniz\t: "))
b= int(input("b sabitini giriniz\t: "))
kok= -b/a 
print("1. dereceden katsayısı {}, sabit sayısı {} olan denklemin kökü : {}".format(a,b,kok))