#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
        保证队列中含有T中字符串个数大于T中相应元素
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in range(len(t)):
            lookup[c]+=1
        left = 0
        right = 0
        min_lenght = 0
        counter=len(t)
        res=''
        while left < len(s):
            if lookup[s[right]]>0:
                counter-=1
            lookup[s[right]]-=1
            right+=1
            while counter==0:
                if min_lenght>right-left:
                    min_lenght = right-left
                    res = s[left:right]
                if lookup[s[left]]==0:
                    counter+=1
                lookup[s[left]]+=1
                left+=1
        return res
