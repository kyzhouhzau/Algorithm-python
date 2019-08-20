#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

#知识点，hash集合
class Solution:
    def isHappy(self, n: int) -> bool:
        seen={1}
        while n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1









x = Solution()
res = x.isHappy(20)
print(res)

