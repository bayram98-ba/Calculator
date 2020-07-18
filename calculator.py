# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 00:32:38 2020

@author: BAYRAM
"""

try:
    reqem1 = int and float(input("Zehmet olmasa birinci reqemi daxil edin:"))
    reqem2 = int and (input("Zehmet olmasa ikinci reqemi daxil edin:"))
    emeliyyat = input("Hansi emeliyyati icra etmek isteyirsiniz:")
    if reqem1==int and float and reqem2==int and  float and emeliyyat =="+":
        print("Netice:",reqem1+reqem2)
    elif reqem1==int and float and reqem2==int and float and emeliyyat =="-":
         print("Netice:",reqem1-reqem2)
    elif reqem1==int and float and reqem2==int and float and emeliyyat =="*":
         print("Netice:",reqem1*reqem2)
    elif reqem1==int and float and reqem2==int and float and emeliyyat =="/":
         print("Netice:",reqem1/reqem2)
except ValueError:
    print("Zehmet olmasa reqem daxil edin...")
except ZeroDivisionError:
    print("Sifira bolmek olmaz...")



