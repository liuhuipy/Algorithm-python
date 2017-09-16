#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

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
        while phead and phead.next and phead.val == phead.next.val:
            phead = phead.next
        if phead is not head:
            phead = head = phead.next
        self.hleft = None
        while phead:
            someHead = 0
            while phead.next and phead.next.val == phead.val:
                someHead = 1
                phead = phead.next
            if someHead == 1:
                if phead.next and self.hleft:
                    self.hleft.next = phead.next
                    phead = self.hleft.next
                elif phead.next and not self.hleft:
                    phead = head = phead.next
                elif not phead.next and not self.hleft:
                    return self.hleft
                else:
                    self.hleft.next = None
                    phead = self.hleft.next
            else:
                self.hleft = phead
                phead = phead.next
        return head


if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(1)
    pnode3 = ListNode(2)
    pnode4 = ListNode(2)
    pnode5 = ListNode(3)
    pnode6 = ListNode(4)
    pnode7 = ListNode(4)
    pnode8 = ListNode(5)
    pnode9 = ListNode(6)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5
    pnode5.next = pnode6
    pnode6.next = pnode7
    pnode7.next = pnode8
    pnode8.next = pnode9

    pnode = ListNode(10)

    solut = Solution()
    resHead = solut.deleteDuplicates(pnode1)
    while resHead:
        print(resHead.val)
        resHead = resHead.next
