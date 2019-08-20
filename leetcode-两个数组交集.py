#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""


class Solution:
    def intersect(self, nums1, nums2):
        hash = {}
        for item in nums2:
            if item not in hash:
                hash[item]=1
            else:
                hash[item]+=1
        res = []
        for item in nums1:
            if item in hash and hash[item]!=0:
               res.append(item)
               hash[item]-=1
        return res

