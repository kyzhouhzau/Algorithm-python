#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
"""
注意特殊情况，就是所有的硬币都丢失
"""
n = int(input())
for i in range(n):
    lis = [int(i) for i in input().split()]
    _sum = sum(lis)
    if _sum%5==0:
        b = int(_sum/5)
        if b==0:
            print(-1)
        else:
            print(b)
    else:
        print(-1)