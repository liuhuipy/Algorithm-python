"""
两数相加II：
    给你两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。你可以假设除了
    数字0之外，这两个数字都不会以零开头。

示例：
    输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 8 -> 0 -> 7

进阶：
    如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

方法1：
    分别遍历两个链表获取数值，两个数值相加后构建链表。
    时间复杂度O(m + n)，空间复杂度O(m + n)
方法2：
    分别遍历两个链表并压入栈中，然后每次出栈构建链表。
    时间复杂度O(m + n)，空间复杂度O(m + n)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        res, temp_num = None, 0
        while s1 or s2 or temp_num:
            num_a = 0 if not s1 else s1.pop()
            num_b = 0 if not s2 else s2.pop()
            sum_num = num_a + num_b + temp_num
            temp_num = sum_num // 10
            num = sum_num % 10
            temp_node = ListNode(num)
            temp_node.next, res = res, temp_node
        return res

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        temp_node1, temp_node2 = l1, l2
        num1, num2 = 0, 0
        while temp_node1:
            num1 = num1 * 10 + temp_node1.val
            temp_node1 = temp_node1.next
        while temp_node2:
            num2 = num2 * 10 + temp_node2.val
            temp_node2 = temp_node2.next

        sum_lis = [s for s in str(num1 + num2)]
        node = ListNode(0)
        res_node = node
        for s in sum_lis:
            node.next = ListNode(int(s))
            node = node.next
        return res_node.next
