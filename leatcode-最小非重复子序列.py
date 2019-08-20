#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

#时间复杂度太高
def lengthOfLongestSubstring(s: str) -> int:
    min = 0
    string = ""
    for i in range(1,len(s)+1):
        for j in range(len(s)-i+1):
            lis = s[j:j+i]
            if len(lis)==len(set(lis)) and len(lis)>min:
                min = len(lis)
                string = lis
    print(string)
#窗口问题：
def lengthOfLongestSubstring_new(s: str) -> int:
    """
    维护一个队列，该队列中不存在重复项，当新加入的为
    重复项则通过remove从左往右删除来使得该重复项不再存在
    :param s:
    :return:
    """
    if not s:return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len+=1
        while s[i] in lookup:
            lookup.remove(s[left])
            left+=1
            cur_len-=1
        if cur_len > max_len:max_len=cur_len
        lookup.add(s[i])
    return max_len

