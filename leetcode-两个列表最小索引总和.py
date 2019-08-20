#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""


class Solution:
    def findRestaurant(self, list1, list2):
        hashdir = {}
        res = {}
        min_num = float("inf")
        for key,value in enumerate(list2):
            hashdir[value]=key
        for index1,item in enumerate(list1):
            index2 = hashdir.get(item)
            if index2!=None:
                num = index1+index2
                res[item]=num
                if num<=min_num:
                    min_num=num
        return [item for item,value in res.items() if value==min_num]

list1 =["Shogun","Tapioca Express","Burger King","KFC"]
list2 =["KFC","Burger King","Tapioca Express","Shogun"]

s = Solution()
s.findRestaurant(list1,list2)




