# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:05:20 2020

@author: BAYRAM
"""


reqem1 =input("Zehmet olmasa birinci reqemi daxil edin:")
reqem2 =input("Zehmet olmasa ikinci reqemi daxil edin:")
emeliyyat = input("Hansi emeliyyati icra etmek isteyirsiniz:")
if reqem1==int and reqem2==int and emeliyyat=="+":
    reqem1=int(input)
    reqem2=int(input)
    print("Netice:",reqem1+reqem2)
elif reqem1==int or float and reqem2==int or float and emeliyyat =="-":
     print("Netice:",reqem1-reqem2)
elif reqem1==int or float and reqem2==int or float and emeliyyat =="*":
    print("Netice:",reqem1*reqem2)
elif reqem1==int or float and reqem2==int or float and emeliyyat =="/":
    print("Netice:",reqem1/reqem2)
elif reqem1==str  and reqem2==int or float and emeliyyat==("+","-","*","/"):
    print("Zehmet olmasa her ikisini de reqem daxil edin....")
elif reqem1==int or float  and reqem2==str and ("+","-","*","/"):
    print("Zehmet olmasa her ikisini de reqem daxil edin....")
elif reqem1==str  and reqem2==str and ("+","-","*","/"):
    print("Zehmet olmasa reqem daxil edin...")
