#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        ss = [str(i) for i in ss]
        lis = []
        self.function(ss,'')
        return lis
    def function(self,arr,res):
        if len(arr)==0:
            print(res)
            return
        else:
            for j in range(len(arr)):
                arr = arr[:j-1]+arr[j+1:]
                self.function(arr,res+arr[j])
s = Solution()
lis = s.Permutation([str(i) for i in "abc"])
print(lis)









