#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个链表，反转链表后，输出链表的所有元素。
'''


class ListNode:

    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return newHead

if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3
    solut = Solution()
    l = []
    head = node1
    while head:
        l.insert(0, head.val)
        head = head.next
    print(l)            #输出[13, 11, 10]
    newHead = solut.ReverseList(node1)
    l = []
    head = newHead
    while head:
        l.insert(0, head.val)
        head = head.next
    print(l)            #输出[10, 11, 13]

