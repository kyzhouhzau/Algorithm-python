#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.perbucket = 10001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self,key):
        return key%self.buckets

    def pos(self,key):
        return key // self.buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [None]*self.perbucket
        self.table[hashkey][self.pos(key)] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = self.hash(key)
        if (not self.table[hashkey]) or self.table[hashkey][self.pos(key)]==None:
            return -1
        else:
            return self.table[hashkey][self.pos(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = None


# Your MyHashMap object will be instantiated and called as such:
