class Otobus:
    plaka:str=""
    nereden:str=""
    nereye:str=""
    koltuk_sayisi:int=0
    _dolu_koltuk_sayisi:int=0



    def__init__(self,nereden,nereye,plaka,koltuk_sayisi)
    self.nereden = nereden
    self.nereye = nereye
    self.plaka = plaka
    self.koltuk_sayisi = koltuk_sayisi

    def bilet_sat(self):
        if self._dolu_koltuk_sayisi<self.koltuk_sayisi:
            self._dolu_koltuk_sayisi -= 1
           
    
    def bilet_iade(self):
        if self._dolu_koltuk_sayisi<0:
            self._dolu_koltuk_sayisi -= 1
        

    
    def durum_yaz(self):
        print("{},{},{},{},{}".format(self.nereden,self.nereye,self.plaka,self.koltuk_sayisi-self._dolu_koltuk_sayisi))
        


