# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:23:12 2020

@author: 14504
"""

import math
def is_prime(number):
    sqrt=int(math.sqrt(number))
    d=0
    for i in range(2,sqrt+1):
        if number % i ==0:
            c = False
            d=1
    if d==0:
        c=True
    return c
    
    
A=input()
a=int(A)
count=0
for t in range(2,a+1):
    if is_prime(t):
        count += 1
print(count)       