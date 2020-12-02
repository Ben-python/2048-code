# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:08:28 2020

@author: 14504
"""

def uses_only(word,string):
    string=string.lower()
    word=word.lower()
    for i in word:
        if not i in string:
            return False
    return True

a=input()
A=a.split(" ")
Word=A[0]
String=A[1]

print(uses_only(Word,String))
        