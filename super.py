# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:56:02 2020

@author: BAYRAM
"""


class Ebeveyn():
    def __init__(self,isim,memleket):
        self.isim=isim
        self.memleket=memleket
    def goster(self):
        print("Adim",self.isim,"ve memleketim",self.memleket)
class Cocuk(Ebeveyn):
    def __init__(self,isim,memleket,yas):
        super(). __init__(isim,memleket)
        self.yas=yas
c1=Cocuk("Bayram","Masalli",22)
print(c1.memleket)
        

c1=Cocuk("Bayram","Masalli")
c1.goster() 

        