#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None

if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(2)
    pnode3 = ListNode(3)
    pnode4 = ListNode(4)
    pnode5 = ListNode(5)
    pnode6 = ListNode(6)
    pnode7 = ListNode(7)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5
    pnode5.next = pnode6
    pnode6.next = pnode7
    pnode7.next = pnode5

    solut = Solution()
    res = solut.detectCycle(pnode1)
    if res:
        print(res.val)

