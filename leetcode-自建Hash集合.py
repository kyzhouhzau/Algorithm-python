#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)]= 1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.hash(key)
        return self.table[hashkey]!=[] and self.table[hashkey][self.pos(key)] == 1

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(2)
param_3 = obj.contains(2)
print(param_3)