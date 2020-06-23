"""
回文链表：
    请判断一个链表是否为回文链表。
示例 1:
    输入: 1->2
    输出: false
示例 2:
    输入: 1->2->2->1
    输出: true

方法1：
    将链表所有节点的值依次存入到一个数组里面，然后判断数组是否为回文数组即可。
    时间复杂度为O(n)，空间复杂度为O(n)。
方法2：
    反转一半链表，然后进行比较。
    时间复杂度为O(n)，空间复杂度为O(1)。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # todo，使用反转
        pass

    def isPalindrome1(self, head: ListNode) -> bool:
        temp_arr = []
        while head:
            temp_arr.append(head.val)
            head = head.next
        start, end = 0, len(temp_arr) - 1
        while start <= end:
            if temp_arr[start] != temp_arr[end]:
                return False
            start, end = start + 1, end - 1
        return True
