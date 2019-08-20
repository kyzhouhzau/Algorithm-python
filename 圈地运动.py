#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

n = int(input())
lis = [int(i) for i in input().split()]
if n<3:
    print(-1)
else:
    for i in range(3,n):
        if 2*max(lis[:i])<sum(lis[:i]):
            print(i)
            break
    else:
        print(-1)

