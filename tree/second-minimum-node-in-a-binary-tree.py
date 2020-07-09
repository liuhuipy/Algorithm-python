"""
二叉树中第二小的节点：
    给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
    如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
    给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:

输入:
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
示例 2:

输入:
    2
   / \
  2   2

输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.first, self.second = float("inf"), float("inf")
        self.findSecondMin(root)
        return self.second if self.second != float("inf") and self.first != self.second else -1

    def findSecondMin(self, node: TreeNode):
        if not node:
            return
        num = node.val
        if self.first < num < self.second:
            self.second = num
        elif self.first > num:
            self.first, self.second = num, self.first
        self.findSecondMin(node.left)
        self.findSecondMin(node.right)
