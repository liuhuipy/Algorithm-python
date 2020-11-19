"""
从前序与中序遍历序列构造二叉树：
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
    你可以假设树中没有重复的元素。

例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

方法：
    dfs
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])
        in_start = 0
        while inorder[in_start] != preorder[0]:
            in_start += 1
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1: in_start + 1], inorder[:in_start])
        node.right = self.buildTree(preorder[in_start + 1:], inorder[in_start + 1:])
        return node


if __name__ == '__main__':
    root = Solution().buildTree([1, 2], [1,2])

    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        print(node.val)
    dfs(root)