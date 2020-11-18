"""
验证二叉搜索树：
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    假设一个二叉搜索树具有如下特征：
        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
    输入:
        2
       / \
      1   3
    输出: true
示例 2:
    输入:
        5
       / \
      1   4
         / \
        3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
         根节点的值为 5 ，但是其右子节点值为 4 。

方法：
    中序遍历，判断是否递增。
    时间复杂度
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.temp_num = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode):
            if not node:
                return True
            r_left = dfs(node.left)
            if node.val <= self.temp_num:
                return False
            self.temp_num = node.val
            r_right = dfs(node.right)
            return r_left and r_right
        return dfs(root)

