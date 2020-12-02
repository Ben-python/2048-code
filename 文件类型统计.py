# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:18:03 2020

@author: 14504
"""


import os
import os.path
path=input()
file_list=os.listdir(".")
labelname={}
for parentdir,dirname,filenames in os.walk(path):
    for filename in filenames:
        if os.path.splitext(filename)[1] in labelname:
            labelname[os.path.splitext(filename)[1]]+=1
        else:
            labelname[os.path.splitext(filename)[1]]=1
    
v_max=max(labelname.values())
for k,v in labelname.items():
    if v==v_max:
        print(k,v)
        

                    