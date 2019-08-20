#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         hashset = set()
#         for item in nums:
#             if item not in hashset:
#                 hashset.add(item)
#             else:
#                 return True
#         return False

#
# class Solution:
#     def singleNumber(self, nums) -> int:
#         hashdir = dict()
#         for item in nums:
#             if item not in hashdir:
#                 hashdir[item]=1
#             else:
#                 hashdir[item]+=1
#         valuekey = {value:key for key,value in hashdir.items()}
#         print(valuekey)
#         return valuekey.get(1)

class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for item in nums1:
            if item in nums2:
               res.append(item)
        print(res)
x = Solution()
y = x.intersection([4,1,2,1,2],[2,2])
print(y)
