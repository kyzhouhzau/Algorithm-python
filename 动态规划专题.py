#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

#1、确定状态
# - 最后一步
# - 子问题
#2、转移方程

def function(x):
    if x==0:
        return 0
    res = float("inf")
    if x>=2:
        res = min(res,function(x))
    elif x>=5:
        res = min(res,function(x))
    elif x>7:
        res = min(res,function(x))
    return res



