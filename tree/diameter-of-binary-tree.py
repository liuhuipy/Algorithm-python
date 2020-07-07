"""
二叉树的直径：
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。

时间复杂度为O(n) n为二叉树节点个数, 空间复杂度为O(log(n))。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_path = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth_tree(node):
            if not node:
                return 0
            left = depth_tree(node.left)
            right = depth_tree(node.right)
            self.max_path = max(left + right, self.max_path)
            return max(left, right) + 1
        depth_tree(root)
        return self.max_path
