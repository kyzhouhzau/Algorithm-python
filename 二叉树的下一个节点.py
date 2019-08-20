#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class TreeLinkNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self,pNode):
        if pNode.right:
            b = pNode.right
            while b.left:
                b = b.left
            return b
        while pNode.next:
            if pNode.next.left==pNode:
                return pNode.next
            pNode =pNode.next
