# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:51:28 2020

@author: 14504
"""
   

def gcd(a,b):
    if a<b:
        a,b=b,a
    c=a % b
    while c !=0:
        a=b
        b=c
        c=a % b
    return b
  
P=input()
p=P.split(" ")
a,b=int(p[0]),int(p[1])
print(gcd(a,b))