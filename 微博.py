# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:37:45 2020

@author: 14504
"""

class Message(object):
    def __init__(self,create_time,author_ID,content):
        self.create_time=create_time
        self.author_ID=author_ID
        self.content=content
        
    def getMessageContent(self):
        return self.content
    def getAuthorID(self):
        return self.author_ID

a1=Message("2020.11.4","DJ","Loss")
print("创建时间:"+a1.create_time)
print("用户ID:"+a1.author_ID)
print("微博内容:"+a1.content)
print("------------")
print (a1.getMessageContent())
print (a1.getAuthorID())
        