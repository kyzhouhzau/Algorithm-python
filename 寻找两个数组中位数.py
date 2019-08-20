#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 对于较短的数组切分，同时可以实现对较长数组的切分
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        lo = 0
        hi = 2 * n
        LMax1 = 0
        LMax2 = 0
        RMin1 = 0
        RMin2 = 0
        while lo <= hi:
            c1 = (lo + hi) // 2
            c2 = m + n - c1
            LMax1 = float("-inf") if c1 == 0 else nums1[(c1 - 1) // 2]
            LMax2 = float("-inf") if c2 == 0 else nums2[(c2 - 1) // 2]
            RMin1 = float("inf") if c1 == 2 * n else nums1[c1 // 2]
            RMin2 = float("inf") if c2 == 2 * m else nums2[c2 // 2]
            if LMax1 > RMin2:
                hi = c1 - 1
            elif LMax2 > RMin1:
                lo = c1 + 1
            else:
                break
        return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2

nums1 = [3]
nums2 = [-2,-1]
s = Solution()
x = s.findMedianSortedArrays(nums1,nums2)
print(x)




