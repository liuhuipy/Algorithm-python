#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:

    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead


if __name__ == "__main__":
    pHead1node1 = ListNode(2)
    pHead1node2 = ListNode(5)
    pHead1node3 = ListNode(8)
    pHead1node1.next = pHead1node2
    pHead1node2.next = pHead1node3

    pHead2node1 = ListNode(3)
    pHead2node2 = ListNode(6)
    pHead2node3 = ListNode(9)
    pHead2node1.next = pHead2node2
    pHead2node2.next = pHead2node3

    solut = Solution()
    solut.Merge(pHead1node1, pHead2node1)
    print(pHead1node1.next.val)     #输出3，说明节点pHead1node1.next指向了pHead2node1节点
    print(pHead2node1.next.val)     #输出5，说明节点pHead2node1.next指向了pHead1node2节点

