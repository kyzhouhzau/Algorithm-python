#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

x = [1,2,3,5,2,1,4,6]
def get_kmax(x,k):
    n = len(x)
    for i in range(k):
        for j in range(n-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    res = x[-k:]
    print(res)

get_kmax(x,5)#时间复杂度K*N










