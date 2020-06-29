"""
反转链表：
    反转一个单链表
示例：
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
解决方案：
    定义一个中间结点，遍历链表中每个结点，将结点元素指向这个中间结点，并每次维护中间结点为当前结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp_node, node = None, head
        while node:
            node.next, temp_node, node = temp_node, node, node.next
        return node