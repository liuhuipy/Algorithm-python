#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入两个链表，找出它们的第一个公共结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        phead, qhead = pHead1, pHead2
        lenpHead1, lenpHead2 = 0, 0
        while phead:
            phead = phead.next
            lenpHead1 += 1
        while qhead:
            qhead = qhead.next
            lenpHead2 += 1

        if lenpHead1 >= lenpHead2:
            for i in range(lenpHead1-lenpHead2):
                pHead1 = pHead1.next
            if pHead1 == pHead2:
                return pHead1
            for i in range(lenpHead2-1):
                pHead1 = pHead1.next
                pHead2 = pHead2.next
                if pHead1 == pHead2:
                    return pHead1
        else:
            for i in range(lenpHead2-lenpHead1):
                pHead2 = pHead2.next
            if pHead1 == pHead2:
                return pHead1
            for i in range(lenpHead1-1):
                pHead1 = pHead1.next
                pHead2 = pHead2.next
                if pHead1 == pHead2:
                    return pHead1
        return None

if __name__ == '__main__':
    pnode1 = ListNode(1)
    pnode2 = ListNode(2)
    pnode3 = ListNode(3)
    pnode4 = ListNode(4)
    pnode5 = ListNode(5)
    pnode6 = ListNode(6)
    pnode1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode4
    pnode4.next = pnode5
    pnode5.next = pnode6

    qnode1 = ListNode(10)
    qnode1.next = pnode4

    solut = Solution()
    resNode = solut.FindFirstCommonNode(pnode1, qnode1)
    if resNode is None:
        print(resNode)
    else:
        print(resNode.val)