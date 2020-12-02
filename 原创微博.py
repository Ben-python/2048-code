# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:08:31 2020

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

class Weibo(Message):
    def __init__(self,create_time,author_ID,content,Reply):
        Message.__init__(self,create_time,author_ID,content)
        self.Reply=Reply
    def GetReplyNums(self):
        Number=0
        for i in self.Reply:
            Number += 1
        print (Number)
    def Delete(self,e):#删除对应评论
        if e in self.Reply:
            self.Reply.remove(e)
        print (self.Reply)
    def EditWeibo(self,a,b):#编辑微博内容
        self.content.replace(a,b)
        print (self.content)

w=Weibo('2020.11.5','me','python第二个作业写完啦',['abcd','太棒了啊','加油加油'])
print("创建时间: "+ w.create_time)
print("用户ID: "+ w.author_ID)
print("微博内容: "+ w.content)
print(w.Reply)
w.GetReplyNums()
w.Delete('abcd')
w.EditWeibo('第二个', '这一周的')

        
    