#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self,head,m,n):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for _ in range(m-1):
            pre = pre.next
        node = None
        cur = pre.next
        for _ in range(n-m+1):
            tmp = cur.next
            cur.next = node
            node = cur
            cur = tmp
        pre.next.next = cur
        pre.next=node
        return dummy.next
