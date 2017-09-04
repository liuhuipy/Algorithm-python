#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
反转链表：
链表的基本形式是：1 -> 2 -> 3 -> null,反转需要变为3 -> 2 -> 1 -> null。
'''

# 单向链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    solut = Solution()
    prev = solut.reverseList(node1)
    while prev:
        print(prev.val)
        prev = prev.next

