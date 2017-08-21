#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        khead = head
        node = head
        for i in range(1,k):
            if node.next == None:
                return None
            else:
                node = node.next

        while True:
            node = node.next
            if node is not None:
                khead = khead.next
            else:
                return khead


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(12)
    node4 = ListNode(13)
    node5 = ListNode(14)
    node6 = ListNode(15)
    node7 = ListNode(16)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    solut = Solution()
    resNode = solut.FindKthToTail(node1, 6)
    if resNode is not None:
        print(resNode.val)
    else:
        print(resNode)


