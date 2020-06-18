"""
删除链表的倒数第K个节点：
    给定一个链表，删除链表的倒数第 k 个节点，并且返回链表的头结点。
示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
方法1：
    两次遍历：第一次遍历获取链表长度，计算从头到倒数第k个节点所需次数；进行第二次遍历该次数来删除该节点。
    时间复杂度为O(n)，空间复杂度为O(1)
方法2：
    一次遍历：
        快慢指针，快指针比慢指针先走k + 1步，快指针走到尾部，慢指针的下一个结点就是倒数第k个结点，将慢指针
        所指的结点的next指针指向该结点的next.next结点。
    时间复杂度为O(n)，空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(-1)
        temp.next, slow, fast = head, temp, temp
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return temp.next

    def removeNthFromEndOne(self, head: ListNode, n: int) -> ListNode:
        node, len_link = head, 0
        while node:
            len_link += 1
            node = node.next
        if len_link < n:
            return head
        need_count = len_link - n
        start_node = ListNode(-1)
        temp = start_node
        start_node.next = head
        for _ in range(need_count):
            temp = temp.next

        temp.next = temp.next.next
        return start_node.next
