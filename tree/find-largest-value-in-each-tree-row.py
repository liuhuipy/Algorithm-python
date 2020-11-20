"""
在每个树行中找最大值：
    您需要在二叉树的每一行中找到最大的值。
示例：
    输入:

          1
         / \
        3   2
       / \   \
      5   3   9

    输出: [1, 3, 9]

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        deque = [root]
        while deque:
            local_max, temp_deque = float("-inf"), []
            while deque:
                node = deque.pop()
                local_max = max(local_max, node.val)
                if node.left:
                    temp_deque.append(node.left)
                if node.right:
                    temp_deque.append(node.right)
            deque = temp_deque
            res.append(local_max)
        return res
