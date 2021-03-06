"""
找树左下角的值：
    给定一个二叉树，在树的最后一行找到最左边的值。
    注意: 您可以假设树（即给定的根节点）不为 NULL。

示例 1:
输入:

    2
   / \
  1   3

输出:
1
 
示例 2:
输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 
方法：
    BFS
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        res = root.val
        while queue:
            res = queue[0].val
            temp_queue = []
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
            queue = temp_queue
        return res
