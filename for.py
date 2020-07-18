# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:30:12 2020

@author: BAYRAM
"""


liste=[1,2,3,4,5]
for sayi in liste:
    print(sayi)
isim="Bayram"
for harf in isim:
    print(harf)

for x in range(10):
    print(x)
for x in range(5,10,2):
    print(x)
isimler=["Ali","Can","Buse"]
for ad in isimler:
    print(ad)
for indeks  in range(len(isimler)):
    print(isimler[indeks])

sayilar=[8,1435,10,7,340]
toplam = 0
for i in sayilar:
    toplam=toplam+i
print(toplam)