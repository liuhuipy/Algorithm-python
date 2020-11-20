"""
二叉树的层序遍历：
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        deque = [root]
        res = []
        while deque:
            temp_res, temp_node = [], []
            for node in deque:
                temp_res.append(node.val)
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            res.append(temp_res)
            deque = temp_node
        return res
