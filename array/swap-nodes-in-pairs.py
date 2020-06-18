"""
两两交换链表中的节点：
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
示例：
    给定1->2->3->4，应该返回2->1->4->3

解决方案：
    每次处理两个节点，设置一个temp节点，temp节点的next指针指向第二个的节点，第二个节点指向第一个节点，第一个节点
    指向第二个节点的下一个节点，temp设置为第一个节点也就是下一次交换的前置节点。
时间复杂度为O(n)，空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = ListNode(-1)
        temp.next, res_node = head, temp
        while head and head.next:
            temp.next = head.next
            next_swap_node = head.next.next
            head.next.next = head
            head.next = next_swap_node
            temp, head = head, next_swap_node
        return res_node.next


