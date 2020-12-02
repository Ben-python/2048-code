# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:14:24 2020

@author: 14504
"""

W=input()
list0=W.split(";")
A=list0[0]
B=list0[1]
p=0
for i in A:
    if i.isspace():
        p=p+1
q=0
for m in B:
    if m.isspace():
        q=q+1
List1=A.split(' ',p)
List2=B.split(' ',q)
List3=[]
for x in List1:
    if not x in List2:
        List3 += [x]
for y in List2:
    if not y in List1:
        List3 += [y]
List4=list(map(int,List3))
List4.sort()
d=len(List4)
c=''
for n in List4:
    c=c+' '+str(n)
c=c[1:]
print(c)
       
