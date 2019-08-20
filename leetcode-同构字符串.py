#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index,s)]==[*map(t.index,t)]

x = Solution()
res=x.isIsomorphic("aba","baa")
print(res)

