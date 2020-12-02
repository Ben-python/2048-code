# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:06:09 2020

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

def test(name,putin,putout):
    if is_reserve(putin)==putout:
        print("%s通过测试"%name)
    else:
        print("%s未通过测试<%s,%s>"%(name,putin,putout))
        
    
#测试点
if __name__=="__main__":
    test("test1","aba","YES")
    test("test2","Aa","YES")
    test("test3","Ka","NO")
    test("test4","KK","YES")
