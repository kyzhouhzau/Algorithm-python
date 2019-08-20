#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
"""
给定字符串写出全排列
思路：递归算法。
"""
def permutation(arr,i,res):
    if i==len(arr):
        if res!="":
            print(res)
        return
    permutation(arr,i+1,res)
    permutation(arr,i+1,res+arr[i])

permutation(["a","b","c","d","e","f","g"],0,"")