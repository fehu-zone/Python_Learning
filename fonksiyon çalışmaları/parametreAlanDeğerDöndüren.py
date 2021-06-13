"""

def Mutlakdeger(a):
    if a<0 :
        a *= -1
    return " MDS: {}" .format(a)
print(Mutlakdeger)
"""

"""
def Topla (a,b):
    return a+b
def Cıkar (a,b):
    return a-b
def Carp (a,b):
    return a*b 
def Bol (a,b):
    return a/b
print (Topla (10,2))
print (Cıkar (10,2))
print (Carp (10,2))
print (Bol (10,2))
"""

"""


def Topla (a,b):
    return a+b
def Cikar (a,b):
    return a-b
def Carp (a,b):
    return a * b 
def Bol (a,b):
    return a/b
print (Topla (10,2))
print (Cikar (10,2))
print (Carp (10,2))
print (Bol (10,2))

secim= input("""
        İŞLEM SEÇENEKLERİ:
       [1]                 : TOPLA
       [2]                 : ÇIKAR
       [3]                 : ÇARP
       [4]                 : BÖL
""")
if secim == "1":
    print (Topla (10,2))
elif secim == "2":
    print(Cikar (10,2))
elif secim == "3":
    print(Carp (10,2))
elif secim == "4":
    print(Bol (10,2))
else:
    print("Belirtilmemiş İşlem")



 """


 def Islem (operator, a, b):
     if operator == "+":
          return a + b
   

    elif operator == "-":
        return a - b

    else:
        return("Hatalı Seçim")
    
    sonuc= Islem("+",5,6 )