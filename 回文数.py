# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:02:33 2020

@author: 14504
"""

def is_reserve(strs):
    #判断字符串是否为回文串
    str=""
    for i in strs:
        if ord(i)<=122 and ord(i)>=97:
            #第2题不要求区分大小写，因此在这里现将大小写字母同化
            i=chr(ord(i)-32)
        else:
            i=i
        str += i
        #输出同化大小写之后的新字符串
    return "YES" if str==str[::-1] else "NO"

def is_letter(strs):
    #判断是否均为英文字母
    for i in strs:
        if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
            a=True
        else:
            a=False
    return True if a==True else False

def is_length(strs):
    #判断字符串的长度
    
    return True if len(strs)<=100 else False 

n=int(input())
i=0
A=[]
while i<=n-1:
    A=A+[input()]
    i=i+1
i=0
whether_break=True
while i<=n-1:
    if is_letter(A[i])==False or is_length(A[i])==False:
        whether_break=False
    i=i+1
i=0
while i<=n-1:
    if whether_break==False:
        break
    print(is_reserve(A[i]))
    i=i+1