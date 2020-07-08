"""
最长同值路径：
    给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
    注意：两个节点之间的路径长度由它们之间的边数表示。
示例 1:
输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_count = 0
        self.computeLongestUnivalue(root)
        return self.max_count

    def computeLongestUnivalue(self, node: TreeNode):
        if not node:
            return None, 0
        left_num, left_count = self.computeLongestUnivalue(node.left)
        right_num, right_count = self.computeLongestUnivalue(node.right)
        l_merge_count = left_count + 1 if left_num == node.val else 0
        r_merge_count = right_count + 1 if right_num == node.val else 0
        count = l_merge_count + r_merge_count
        self.max_count = max(count, self.max_count)
        big_count = max(l_merge_count, r_merge_count)
        return node.val, big_count
