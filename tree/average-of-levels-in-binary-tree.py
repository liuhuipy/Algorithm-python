"""
二叉树的层平均值：
    给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

方法1：
    BFS。遍历每层并计算平均值。
方法2：
    BFS。用两个数组记录每层元素个数和元素之和，最后分别计算平均值。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        res = []
        while queue:
            temp, temp_queue = [], []
            while queue:
                node = queue.pop()
                temp.append(node.val)
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
            queue = temp_queue
            if temp:
                res.append(sum(temp) / len(temp))
        return res

    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        self.count, self.res = [], []
        self.helper(root, 0)
        return [self.res[i] / self.count[i] for i in range(len(self.res))]

    def helper(self, node: TreeNode, depth):
        if not node:
            return
        if len(self.count) <= depth:
            self.count.append(1)
            self.res.append(node.val)
        else:
            self.count[depth] += 1
            self.res[depth] += node.val
        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)
