#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
n = int(input())
max_lis = list(map(int,input().split()))
all = []
count = 0
while count<n:
    count+=1
    alis = list(map(int,input().split()))
    for i in range(len(alis)):
        if alis[i]<=max_lis[i]:
            all.append(1)
            break

print(len(all))



