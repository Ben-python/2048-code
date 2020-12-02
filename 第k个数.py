# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:01:23 2020

@author: 14504
"""

def NumberK(string,i,j,k):
    number=string[i-1:j:1]
    Number=list(map(int,number))
    Number.sort()
    Number_selected=Number[k-1]
    return Number_selected

List=input()
List_origin=input()
List0=List.split(" ")
n,m=List0[0],List0[1]
n,m=int(n),int(m)
List_processed=List_origin.split(" ")
i=0
list_total=[]
while i <= m-1:
    a=input()
    list_total += [a]
    i=i+1
i=0
while i <= m-1:
    list_split2=list_total[i].split(" ")
    list_total[i]=list(map(int,list_split2))
    i=i+1
q=0
while q <= m-1:
    i=list_total[q][0]
    j=list_total[q][1]
    k=list_total[q][2]
    print(NumberK(List_processed,i,j,k))
    q += 1
    

