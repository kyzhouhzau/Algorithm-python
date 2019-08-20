#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
def binary_search(alist,start,end,target):
    n = len(alist)
    if n>0:
        mid = (end-start) // 2
        if alist[mid]==target:
            return True
        if alist[mid]>target:
            alist = alist[:end]
            return binary_search(alist,0,mid,target)
        elif alist[mid]<target:
            alist = alist[start:]
            return binary_search(alist,mid+1,n,target)
    return False

def binary_search_v2(alist,item):
    n = len(alist)
    start = 0
    end = n-1
    while start<=end:
        mid = (start+end)//2
        if alist[mid]==item:
            return True
        if alist[mid]>item:
            end = mid-1
        else:
            start = mid+1
    return False


# 第一次练习，二分查找：

def binary_search_v3(alist,item):
    start = 0
    end = len(alist)-1
    while start<=end:
        mid = (start+end)//2
        if alist[mid]==item:
            return True
        if alist[mid]>item:
            end = mid-1
        else:
            start = mid+1
    return False





x = [2, 3, 4, 5, 6]
res = binary_search(x,0,len(x),4)
ress = binary_search_v2(x,4)
print(ress)
print(res)


