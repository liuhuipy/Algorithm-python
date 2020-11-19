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

方法1：
    dfs
方法2：TODO
    bfs
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
        n = len(preorder)
        temp_map = {num: i for i, num in enumerate(inorder)}

        def dfs(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode:
            if pre_start > pre_end:
                return None
            pre_root_num = preorder[pre_start]
            in_root_index = temp_map[pre_root_num]
            move_size = in_root_index - in_start
            node = TreeNode(pre_root_num)
            node.left = dfs(pre_start + 1, pre_start + move_size, in_start, in_root_index - 1)
            node.right = dfs(pre_start + move_size + 1, pre_end, in_root_index + 1, in_end)
            return node

        return dfs(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    root = Solution().buildTree([1, 2, 3], [3, 2, 1])

    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        print(node.val)
    dfs(root)