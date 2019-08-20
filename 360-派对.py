#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
n = int(input())
for i in range(n):
    lis = [int(i) for i in input().split()]
    lis.sort()
    if lis[0]+lis[1]>lis[2]//2:
        print(sum(lis)//3)
    else:
        print(lis[0]+lis[1])



