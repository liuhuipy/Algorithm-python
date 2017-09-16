#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given   and x = 3, return   .
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        leftHead = ListNode(0)
        firstHead, lastHead = head, head
        leftHead.next = head
        hasFirst = 0
        while head:
            if head.val < x and hasFirst == 0:
                hasFirst = 1
                firstHead = head
            if head.val < x and leftHead.next is not head:
                lastHead.next = head.next
                temp = leftHead.next
                leftHead.next = head
                leftHead = head
                leftHead.next = temp
                head = lastHead.next
            elif head.val < x and leftHead.next is head:
                leftHead = leftHead.next
                lastHead = head
                head = head.next
            else:
                lastHead = head
                head = head.next
        return firstHead

if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(4)
    pnode3 = ListNode(3)
    pnode4 = ListNode(2)
    pnode5 = ListNode(5)
    pnode6 = ListNode(2)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5
    pnode5.next = pnode6

    solut = Solution()
    phead = solut.partition(pnode1, 3)
    while phead:
        print(phead.val)
        phead = phead.next

