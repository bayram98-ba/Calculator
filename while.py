# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:25:29 2020

@author: BAYRAM
"""


gizli_kelime="Bayram"
tahmin=""
tahmin_sayisi=0
tahmin_limit=3
tahmin_cikis=False
while tahmin!=gizli_kelime and not(tahmin_cikis):
    if tahmin_sayisi<tahmin_limit:
        tahmin=input("Tahmin girin:")
        tahmin_sayisi +=1
    else:
        tahmin_cikis=True
if tahmin_cikis:
        print("Teessuf...")
else:
        print("Tebrikler!!!")
