"""
二叉树的所有路径：
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    说明: 叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

方法：
    DFS。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res_arr = []

        def helper(node: TreeNode, path: str):
            if node is not None:
                path += str(node.val) if node is root else "->" + str(node.val)
                if not node.left and not node.right:
                    res_arr.append(path)
                    return
                helper(node.left, path)
                helper(node.right, path)

        helper(root, "")
        return res_arr
