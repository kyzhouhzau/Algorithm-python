#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
"""
注意像素点大小为1
"""
# t = int(input())
# for i in range(t):
#     n = int(input())
#     num = 0
#     for j in range(n):
#         lis = list(map(int,input().split()))
#         x1,y1,x2,y2 = lis
#         num+=(x2-x1+1)*(y2-y1+1)
#     print(num)

t = int(input())
for i in range(t):
    n = int(input())
    _sum = 0
    for j in range(n):
        lis  = [int(i) for i in input().split()]
        x1,y1,x2,y2 = lis
        x = (x1,x2)
        y = (y1,y2)
        _sum+=(max(x)-min(x)+1)*(max(y)-min(y)+1)
    print(_sum)