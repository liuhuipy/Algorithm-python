"""
奇偶链表：
    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
示例:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
示例 2:
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL
todo: 方法解析
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
