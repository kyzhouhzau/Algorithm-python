#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

def bubble_sort(alist):
    """
    1、比较相邻元素，如果逆序则交换
    2、对每一对相邻元素做同样操作
    3、针对所有元素重复以上操作
    4、重复每次对越来越少的元素重复以上操作
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(n-1):
        count=0
        for i in range(n-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count+=1
        if count==0:
            break

def quick_sort(alist,start,end):
    """
    1、基值
    2、两个指针
    :param alist:
    :param start:
    :param end:
    :return:
    """
    if start>=end:
        return
    first = start
    last = end
    base = alist[0]
    while first<last:
        while first<last and base <=alist[last]:
            last-=1
        alist[first]=alist[last]

        while first<last and base >alist[first]:
            first+=1

        alist[last]=alist[first]

    alist[first]=base

    quick_sort(alist,first,first-1)
    quick_sort(alist,first+1,last)

def select_sort(alist):
    """
    1、对于无序序列选择最小的与该无序序列第一个交换
    2、序列被分成有序和无序两个部分，继续从无序中选择最小的与无序第一个交换，知道去不有序
    :param alist:
    :return:
    """
    n = len(alist)
    for i in range(n-1):
        min_index = 0
        for j in range(i+1,n):
            if alist[j]<alist[min_index]:
                min_index=j
        alist[i],alist[min_index] = alist[min_index],alist[i]

def insert_sort(alist):
    """
    1、将序列分成有序和无序两个部分。
    2、依次从无序部分取出一个与有序部分比较，从而找到正确位置插入
    :param alist:
    :return:
    """
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]

if __name__=="__main__":
    x = [2,3,1,4,6,8,10]
    # quick_sort(x,0,len(x)-1)
    bubble_sort(x)
    print(x)
