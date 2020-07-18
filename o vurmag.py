# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:40:31 2020

@author: BAYRAM
"""


reqem=int(input("Bir reqem girin:"))
if 0<reqem<=10:
    reqem*5 and print(reqem*5)
if 100>= reqem >=10:
    reqem*3 and print(reqem*3)
if reqem == 0:
    print("0-a vurmag deye bir sey yoxdu qaqasssss")
if reqem>100:
    print("Bu reqem cox boyukdur.")
else:
    print("Teessuf...")