# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:53:09 2020

@author: 14504
"""

import jieba
def full_mode(content):
    seg_list=jieba.cut(content,cut_all=True)
    return ('Full Mode:'+'/'.join(seg_list))

def default_mode(content):
    seg_list=jieba.cut(content,cut_all=False)
    return ('Default Mode:'+'/'.join(seg_list))

def cut_for_search(content):
    seg_list=jieba.cut_for_search(content)
    return ('Search Mode:'+'/'.join(seg_list))


def dic_wordcount(content):
    seg_list=jieba.cut(content,cut_all=False)
    WordCount={}
    for i in seg_list:
        if i in WordCount:
            WordCount[i]+=1
        else:
            WordCount[i]=1
    WordCountlist=[(k,v) for k,v in WordCount.items()] 
    return WordCountlist 

def test_cutout(name,in_put,out_come):
    if dic_wordcount(in_put)==out_come:
        print('%s通过测试'%name)
    else:
        print('%s未能通过测试'%name)

test_cutout('test1','对围绕马保国所发生的一系列闹剧，不是一笑了之那么简单。如果靠哗众取宠就可以风生水起，靠招摇撞骗就能拓展商业版图，这是什么样的价值取向？马保国背后的人到底想干什么？明眼人都清楚，无非就是商业利益。放任“审丑”成为流行，让招摇撞骗大行其道，这本身就是对社会风气的伤害，特别对于尚缺乏判断力的未成年人，这是对价值体系的毒化。这场以马保国为主题的闹剧，该收场了。',[('对', 3), ('围绕', 1), ('马', 2), ('保国', 3), ('所', 1), ('发生', 1), ('的', 7), ('一系列', 1), ('闹剧', 2), ('，', 9), ('不是', 1), ('一笑了之', 1), ('那么', 1), ('简单', 1), ('。', 4), ('如果', 1), ('靠', 2), ('哗众取宠', 1), ('就', 2), ('可以', 1), ('风生水', 1), ('起', 1), ('招摇撞骗', 2), ('能', 1), ('拓展', 1), ('商业', 1), ('版图', 1), ('这是', 1), ('什么样', 1), ('价值', 1), ('取向', 1), ('？', 2), ('背后', 1), ('人', 1), ('到底', 1), ('想干什么', 1), ('明眼人', 1), ('都', 1), ('清楚', 1), ('无非', 1), ('就是', 2), ('商业利益', 1), ('放任', 1), ('“', 1), ('审丑', 1), ('”', 1), ('成为', 1), ('流行', 1), ('让', 1), ('大行其道', 1), ('这', 2), ('本身', 1), ('社会风气', 1), ('伤害', 1), ('特别', 1), ('对于', 1), ('尚', 1), ('缺乏', 1), ('判断力', 1), ('未成年人', 1), ('是', 1), ('价值体系', 1), ('毒化', 1), ('这场', 1), ('以马', 1), ('为', 1), ('主题', 1), ('该', 1), ('收场', 1), ('了', 1)])
