# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:12:21 2020

@author: 14504
"""
import re
def substitution(mode_string,sub_string,filename):
    try: 
        with open(filename,"r+")as fn:
            data=fn.readlines()
            for eachdata in data:
                a=re.sub(mode_string,sub_string,eachdata)
                fn.writelines(a)                
    except:
        return "出现错误"
    
mode_string=input()
sub_string=input()
filename=input()
substitution(mode_string,sub_string,filename)


