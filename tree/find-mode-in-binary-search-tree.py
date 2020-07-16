"""
二叉搜索树中的众树：
    给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
    假定 BST 有如下定义：
        结点左子树中所含结点的值小于等于当前结点的值
        结点右子树中所含结点的值大于等于当前结点的值
    左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.max_count = 0
        self.temp_count, self.temp_n = 0, None
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node: TreeNode):
        if not node:
            return
        self.helper(node.left)
        if node.val == self.temp_n:
            self.temp_count += 1
        else:
            self.temp_n = node.val
            self.temp_count = 1
        if self.temp_count == self.max_count:
            self.res.append(node.val)
        elif self.temp_count > self.max_count:
            self.max_count = self.temp_count
            self.res = [node.val]
        self.helper(node.right)
