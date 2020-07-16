"""
二叉搜索树的最小绝对差：
    给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

提示：
    树中至少有 2 个节点。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference1(self, root: TreeNode) -> int:
        self.res = float("inf")
        self.helper(root)
        return self.res

    def helper(self, node: TreeNode) -> (any, any):
        if not node:
            return None, None
        temp_left_min, temp_left_max = self.helper(node.left)
        temp_right_min, temp_right_max = self.helper(node.right)
        if temp_left_max is not None:
            self.res = min(self.res, node.val - temp_left_max)
        if temp_right_min is not None:
            self.res = min(self.res, temp_right_min - node.val)
        return (
            temp_left_min if temp_left_min is not None else node.val,
            temp_right_max if temp_right_max is not None else node.val
        )