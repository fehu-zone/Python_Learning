

class Robot():
    def __init__(self,isim):
        self.isim = isim 
    

    def kendini_tanit(self):
        print("Benim Adım {}".format(self.isim))
                
class asci_robot(Robot):


    def __init__(self, isim, yemek_sayisi , hazirlama_hizi):
        super().__init__(isim)
        self.yemek_sayisi = yemek_sayisi
        self.hazirlama_hizi= hazirlama_hizi

    def yemek_say(self):
        print("{} Şuanda {} çeşit yemek yapabilir".format(self.isim,self.yemek_sayisi))


robo_1 = Robot("Andro")
robo_2 = asci_robot("Wall-o", 50, 40)

print(robo_2.isim)
print(robo_2.yemek_sayisi)
print(robo_2.hazirlama_hizi)

robo_2.kendini_tanit()
robo_2.yemek_say()



