"""
平衡二叉树：
    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

时间复杂度为O(n) n为二叉树节点个数, 空间复杂度为O(log(n))。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = True

    def isBalanced(self, root: TreeNode) -> bool:
        def child_balance(node):
            if not node:
                return 0
            left = child_balance(node.left)
            right = child_balance(node.right)
            if abs(left-right) > 1:
                self.res = False
            return max(left, right) + 1
        child_balance(root)
        return self.res
