#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
n, m, x, k = map(int,input().split())
score = map(int,input().split())

c = sum(score)
uc= n-c
if c >=uc:
    money = n*m-uc*x-(c-uc)*k
else:
    money = n*m-uc*x

print(money)