"""
相交链表：
    编写一个程序，找到两个单链表相交的起始节点。

方法1：
    分两次遍历：
        第一次遍历两个链表，获取长度分别为m和n，获取m、n中较长的（这里假设m>n）；
        第二次遍历较长的链表先开始，遍历m-n个元素后，两个链表一起遍历接下来的元素，直到遍历的两个节点元素相同为止。
    时间复杂度为O(m+n)，空间复杂度为O(1)
方法2：
    双指针法链表拼接：
        假设两个链表A, B的长度分别为m、n，相交的结点位置分别为两个链表的第a, 第b位结点。易知，两个链表相交结点后的结点长度必相等，即
        m - a = n - b， 得到m + b = a + n。
        同时循环遍历A，B的结点：当A访问尾部结点后，再访问B的头部结点，共访问m + b次访问到相交结点；当B访问尾部结点后，再访问A的头部结点，共
        访问n + a次访问到相交结点。
    时间复杂度为O(m+n)，空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a

    def getIntersectionNodeOne(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_a, node_b = headA, headB
        len_a, len_b = 0, 0
        while node_a:
            len_a += 1
            node_a = node_a.next

        while node_b:
            len_b += 1
            node_b = node_b.next

        if len_a >= len_b:
            quick_node, slow_node, cha = headA, headB, len_a - len_b
        else:
            quick_node, slow_node, cha = headB, headA, len_b - len_a

        while cha > 0:
            quick_node = quick_node.next
            cha -= 1

        while quick_node:
            if quick_node == slow_node:
                return quick_node
            quick_node, slow_node = quick_node.next, slow_node.next
