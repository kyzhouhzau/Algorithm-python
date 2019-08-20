#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution():
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        x1 = ''
        while l1:
            x1 +=str(l1.val)
            l1 = l1.next
        x2 = ''
        while l2:
            x2 += str(l2.val)
            l2  = l2.next

        res = int(x1[::-1])+int(x2[::-1])
        res = str(res)[::-1]

        ans = ListNode(int(res[0]))
        ans1 = ans
        for i in res[1:]:
            ans.next = ListNode(int(i))
            ans = ans.next
        return ans1

