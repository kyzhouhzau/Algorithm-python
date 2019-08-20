#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashdir = {}
        for i,item in enumerate(s):
            if item not in hashdir:
                hashdir[item]=0
            else:
                hashdir[item]+=1
        for key,value in hashdir.items():
            if value==0:
                return s.index(key)
        else:
            return -1


s = Solution()
res = s.firstUniqChar("leetcode")
print(res)
