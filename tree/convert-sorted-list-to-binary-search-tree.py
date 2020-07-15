"""
有序链表转换二叉搜索树：
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

方法：
    链表值添加到数组 + 递归。

"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        return self.helper(nums)

    def helper(self, nums: List[int]):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums[:mid])
        node.right = self.helper(nums[mid + 1:])
        return node
