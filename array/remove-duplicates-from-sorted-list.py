"""
删除排序链表中的重复元素：
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

解决方案：
    遍历每个结点和下一个结点，判断结点val是否相等，如果相等则将该结点next指向下一个结点的next（即删除下一个结点），否则往下一个元素遍历。
时间复杂度为O(n)，空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
