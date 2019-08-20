#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
# n的阶乘
def getFactorial(n):
    if n==1:
        return 1
    return n*getFactorial(n-1)

# 求字符串所有子序列

def printAllSubsquence(test, i, res):
    if i == len(test):
        print(res)
        return
    printAllSubsquence(test, i+1, res)
    printAllSubsquence(test, i+1, res + test[i])

printAllSubsquence(["b","c","d"],0,"")