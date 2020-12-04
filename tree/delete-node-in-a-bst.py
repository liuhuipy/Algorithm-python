"""
删除二叉树搜索树中的节点：
    给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
    返回二叉搜索树（有可能被更新）的根节点的引用。
    一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。
    说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
示例:
    root = [5,3,6,2,4,null,7]
    key = 3

        5
       / \
      3   6
     / \   \
    2   4   7
    给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
        5
       / \
      4   6
     /     \
    2       7
    另一个正确答案是 [5,2,6,null,4,null,7]。
        5
       / \
      2   6
       \   \
        4   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def helper(grant_father: TreeNode, parent: TreeNode, node: TreeNode, max_node: bool) -> TreeNode:
            if max_node:
                if node.right:
                    return helper(grant_father, node, node.right, True)
                parent.right = node.left
                node.left = grant_father.left
                node.right = grant_father.right
                return node
            else:
                if node.left:
                    return helper(grant_father, node, node.left, False)
                parent.left = node.right
                node.right = grant_father.right
                node.left = grant_father.left
                return node

        def dfs(node: TreeNode):
            if not node:
                return
            if node.val == key:
                if node.right:
                    if not node.right.left:
                        temp = node.left
                        node = node.right
                        node.left = temp
                        return node
                    return helper(node, node, node.right, False)
                if node.left:
                    if not node.left.right:
                        temp = node.right
                        node = node.left
                        node.right = temp
                        return node
                    return helper(node, node, node.left, True)
                return None
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        return dfs(root)
