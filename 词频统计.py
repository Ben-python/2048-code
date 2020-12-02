# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:24:32 2020

@author: 14504
"""

A=input()
a=A.split(' ')
WordCount={}
for i in a:
    if i in WordCount:
        WordCount[i] += 1
    else:
        WordCount[i] = 1
print(WordCount[1][1])
WordCountlist=[(k,v) for k,v in WordCount.items()]        
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j][1] >= nums[j + 1][1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
bubble_sort(WordCountlist)
Countest=WordCountlist[-1][0]
i=0
for i in range(len(WordCountlist)-1):
    if WordCountlist[-1-i][1] == WordCountlist[-2-i][1]:
        Countest += " " + WordCountlist[-2-i][0] 
    else:
        break

print(Countest)