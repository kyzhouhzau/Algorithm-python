#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

#方法一中心扩散
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         res = ''
#         for i in range(n):
#             odd_str,odd_length = self.kuosan(s,i,i)
#             even_star,even_length = self.kuosan(s,i,i+1)
#             max_str = odd_str if odd_length>even_length else even_star
#             if len(max_str)>=len(res):
#                 res = max_str
#         return res
#
#     def kuosan(self,s,left,right):
#         while left>=0 and right<len(s) and s[left] == s[right]:
#             left-=1
#             right+=1
#         return s[left+1:right],right-left-1

#方法二
#动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left = 0
        right = n
        res = ''
        max_len = 0
        for left in range(n):
            for right in range(1,n):
                target = s[left:right]
                if len(target)<=3 and target[0] == target[-1]:
                    if len(target)>max_len:
                        max_len = len(target)
                        res = target







x = Solution()
res = x.longestPalindrome("cbbd")
print(res)






