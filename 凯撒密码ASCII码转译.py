# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:04:52 2020

@author: 14504
"""

a=input()
b=input()
B=int(b)
s=""
for i in a:
    p=ord(i)
    if p<=122 and p>=97 or p<=90 and p>=65:
        c=B%26
        f=p+c
        if p>=65 and f<=90 or p>=97 and f<=122:
            q=chr(p+c)
        else:
            q=chr(p+c-26)
        t=q
    else:
        t=i   
    s=s+t
print(s)