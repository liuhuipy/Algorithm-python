#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        phead = ListNode(0)
        phead.next = head
        p = phead
        for i in range(m-1):
            p = p.next

        curr = p.next
        for i in range(n-m):
            temp = curr.next
            curr.next = temp.next
            temp.next = p.next
            p.next = temp

        return phead.next


if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(2)
    pnode3 = ListNode(3)
    pnode4 = ListNode(4)
    pnode5 = ListNode(5)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5

    solut = Solution()
    resHead = solut.reverseBetween(pnode1, 2, 4)
    while resHead:
        print(resHead.val)
        resHead = resHead.next

