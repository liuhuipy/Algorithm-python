#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        phead = head
        while phead:
            while phead.next and phead.next.val == phead.val:
                phead.next = phead.next.next
            phead = phead.next
        return head


if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(1)
    pnode3 = ListNode(2)
    pnode4 = ListNode(3)
    pnode5 = ListNode(3)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5

    solut = Solution()
    res = solut.deleteDuplicates(pnode1)
    print(res)
