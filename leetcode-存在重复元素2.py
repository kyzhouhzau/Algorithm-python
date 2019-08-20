#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        hashset  = set()
        index = 0
        for i,item in enumerate(nums):
            if item in hashset:
                return True
            hashset.add(item)
            if len(hashset)>k:
                hashset.remove(nums[index])
                index+=1
        return False

nums = [1,2,3,1,2,3]
k =2
s = Solution()
res = s.containsNearbyDuplicate(nums,k)
print(res)
