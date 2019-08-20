#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
#用递归的想法当前节点与上下限比较，并递归的对子树进行

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self,root):
        def helper(node,lower,upper):
            if not node:
                return True
            if node.val> lower and node.val<upper:
                return helper(node.left,lower,node.val) and helper(node.val,node.val,upper)
            else:
                return False

        return helper(root,float("-inf"),float("inf"))

#利用中序遍历
class Solution2:
    def isValidBST(self,root):
        res = []
        def midorder(root):
            if not root:
                return
            midorder(root.left)
            res.append(root.val)
            midorder(root.right)
        midorder(root)
        return res == sorted(res) and len(set(res))==len(res)

