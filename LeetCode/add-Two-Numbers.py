#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        newNode = ListNode(0)
        lastNode = newNode
        addNum = 0
        while l1 and l2:
            nodeSum = l1.val + l2.val + addNum
            addNum = nodeSum // 10
            newNodeNum = nodeSum % 10
            aNode = ListNode(newNodeNum)
            lastNode.next = aNode
            lastNode = aNode
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2 and addNum >= 1:
            aNode = ListNode(addNum)
            lastNode.next = aNode
            return newNode.next
        while l1:
            nodeSum = l1.val + addNum
            addNum = nodeSum // 10
            newNodeNum = nodeSum % 10
            aNode = ListNode(newNodeNum)
            lastNode.next = aNode
            lastNode = aNode
            l1 = l1.next
        while l2:
            nodeSum = l2.val + addNum
            addNum = nodeSum // 10
            newNodeNum = nodeSum % 10
            aNode = ListNode(newNodeNum)
            lastNode.next = aNode
            lastNode = aNode
            l2 = l2.next
        if addNum >= 1:
            aNode = ListNode(addNum)
            lastNode.next = aNode
        return newNode.next

if __name__ == '__main__':
    pnode1 = ListNode(2)
    pnode2 = ListNode(4)
    pnode3 = ListNode(3)
    pnode1.next = pnode2
    pnode2.next = pnode3

    qnode1 = ListNode(9)
    qnode2 = ListNode(9)
    qnode3 = ListNode(4)
    qnode1.next = qnode2
    qnode2.next = qnode3

    solut = Solution()
    resHead = solut.addTwoNumbers(pnode1, qnode1)
    while resHead:
        print(resHead.val)
        resHead = resHead.next
