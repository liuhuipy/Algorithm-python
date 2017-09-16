#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        pHead = ListNode(0)
        cur = pHead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2

        return pHead.next


if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(2)
    pnode3 = ListNode(3)
    pnode4 = ListNode(4)
    pnode5 = ListNode(5)
    pnode6 = ListNode(6)
    pnode7 = ListNode(7)
    pnode1.next = pnode3
    pnode3.next = pnode5
    pnode5.next = pnode7

    pnode2.next = pnode4
    pnode4.next = pnode6

    solut = Solution()
    resNode = solut.mergeTwoLists(pnode1, pnode2)
    while resNode:
        print(resNode.val)
        resNode = resNode.next
