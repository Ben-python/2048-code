A = {'a':7, 'b':2, 'c':3, 'd':1}

Alist = [(k, v) for k, v in A.items()]

def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j][1] > nums[j + 1][1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort(Alist))
