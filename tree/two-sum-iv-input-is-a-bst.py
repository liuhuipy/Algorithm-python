"""
两数之和IV - 输入BST：
    给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
输出: True
 

案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.res = []
        self.helper(root)
        left, right = 0, len(self.res) - 1
        while left < right:
            if self.res[left] + self.res[right] == k:
                return True
            if self.res[left] + self.res[right] > k:
                right -= 1
            else:
                left += 1
        return False

    def helper(self, node: TreeNode):
        if not node:
            return
        self.helper(node.left)
        self.res.append(node.val)
        self.helper(node.right)
