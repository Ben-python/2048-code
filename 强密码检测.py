# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:24:11 2020

@author: 14504
"""

a=input()
A1,A2,A3,A4=False,False,False,False
for i in a:
    if 65<=ord(i)<=90:
        A1=True
    if 97<=ord(i)<=122:
        A2=True
    if 48<=ord(i)<=57:
        A3=True
    if ord(i)==44 or ord(i)==46 or ord(i)==95:
        A4=True
if A1==True and A2==True and A3==True and A4==True:
    print(True)
else:
    print(False)
    