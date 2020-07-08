"""
另一个树的子树：
    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
    s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = t
        self.res = False
        self.checkHead(s)
        return self.res

    def checkHead(self, s: TreeNode) -> any:
        if not s:
            return
        if s.val == self.t.val and self.checkChild(s, self.t):
            self.res = True
        self.checkHead(s.left)
        self.checkHead(s.right)

    def checkChild(self, s: TreeNode, t: TreeNode) -> bool:
        if (not s and t) or (not t and s) or (s and t and s.val != t.val):
            return False
        if not s:
            return True
        return self.checkChild(s.left, t.left) is not False and self.checkChild(s.right, t.right) is not False
