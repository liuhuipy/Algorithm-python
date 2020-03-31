#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Node:

    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class LinkedList:

    def __init__(self):
        self.head = 0

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def get_length(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def init_list(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def __getitem__(self, key):
        if self.is_empty():
            print('linklist is empty')
            return
        if key < 0 or key > self.get_length():
            raise IndexError
        else:
            return self.getitem(key)

    def getitem(self, index):
        j = 0
        p = self.head
        while p.next != 0 and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.data
        else:
            print('target is not exist!')

    def delete(self, index):
        if self.is_empty() or index < 0 or index > self.get_length():
            print('linklist is empty or index is bad')
            return
        if index == 0:
            pass



