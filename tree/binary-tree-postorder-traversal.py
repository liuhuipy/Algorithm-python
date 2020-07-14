"""
二叉树的后序遍历：
    给定一个二叉树，返回它的后序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

方法1：
    递归
方法2：
    迭代，按根-右-左取元素，然后将结果进行反转。

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            temp = queue.pop()
            res.append(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        return res[::-1]

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node: TreeNode) -> None:
        if not node:
            return
        self.helper(node.left)
        self.helper(node.right)
        self.res.append(node.val)
