# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:52:33 2020

@author: 14504
"""

string=input()
T=""
length=len(string)
i=0
while i <=length-1:
    if i==0:
        if 65<=ord(string[0])<=90:
            T=string[0]
        else:
            T=chr(ord(string[0])-32)
    elif string[i]==" ":
        if 65<=ord(string[i+1])<=90:
            T= T+string[i+1]
        else:
            T= T+chr(ord(string[i+1])-32)
    i=i+1
      
print(T)   