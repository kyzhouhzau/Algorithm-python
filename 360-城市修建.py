#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
n = int(input())
hight = float('-inf')
weights = float('-inf')
_hight = float('inf')
_weights = float('inf')
for i in range(n):
    lis = [int(i) for i in input().split()]
    if lis[0]>hight:
        hight=lis[0]
    if lis[1]>weights:
        weights=lis[1]
    if lis[0]<_hight:
        _hight=lis[0]
    if lis[1]<_weights:
        _weights=lis[1]
hight=hight-_hight
weights = weights-_weights
if hight>weights:
    print(hight**2)
else:
    print(weights**2)