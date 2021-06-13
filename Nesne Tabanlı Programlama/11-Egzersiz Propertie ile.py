class Uye:
    @property
    def Dtarihi(self):
        return self.__Dtarihi

    @Dtarihi.setter
    def Dtarihi(self,value):
        self.Dtarihi = value 

u1= Uye()
u1.Dtarihi = 2023
print(u1.Dtarihi)
