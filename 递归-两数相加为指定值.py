#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
"""
思路：考虑当加上第i个元素，和不加第i个元素的时候的情况。
"""
def function(arr,i,res):
    if res==0:
        return True
    elif i==0:
        return arr[0]==res
    elif arr[i]>res:
        return function(arr,i-1,res)
    else:
        A = function(arr,i-1,res)
        B = function(arr,i-1,res-arr[i])
        return A or B
arr = [2,13,1,5,3,5,7]
r = function(arr,len(arr)-1,10)
print(r)


