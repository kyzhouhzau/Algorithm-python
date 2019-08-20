#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

def quick_sort(alist,first,end):
    if end>=first:
        return
    base = alist[first]
    low = first
    high = end

    while low<high:
        while low<high and alist[high]>=base:
            high-=1
        alist[low]=alist[high]
        while low<high and alist[low]<base:
            low+=1
        alist[high]=alist[low]
    alist[low]=base
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,end)

