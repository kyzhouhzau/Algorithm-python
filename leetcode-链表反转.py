#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self,head):
        if head is None:return
        pre = None
        while head.next:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        head.next = pre
        return head



