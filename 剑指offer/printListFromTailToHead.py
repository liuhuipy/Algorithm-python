#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个链表，从尾到头打印链表每个节点的值。
返回从尾部到头部的列表值序列，例如[1,2,3]
'''

class ListNode:

    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:

    def printListFromTailToHead(self, listNode):
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3
    solut = Solution()
    print(solut.printListFromTailToHead(node1))
