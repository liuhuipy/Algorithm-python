"""
对称二叉树：
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
方法1：
    迭代。使用队列每次插入左右节点对称位置的节点，然后判断。
方法2：
    递归。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root or not (root.left or root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            right = queue.pop()
            left = queue.pop()
            if left is None and right is None:
                continue
            if not (left and right) or left.val != right.val:
                return False
            queue.append(left.right)
            queue.append(right.left)
            queue.append(left.left)
            queue.append(right.right)
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMetric(root.left, root.right)

    def isMetric(self, l: TreeNode, r: TreeNode) -> bool:
        if (not l and r) or (not r and l) or (l and r and l.val != r.val):
            return False
        if not l:
            return True
        return self.isMetric(l.left, r.right) and self.isMetric(l.right, r.left)
