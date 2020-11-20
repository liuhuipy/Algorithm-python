"""
N叉树的层序遍历：
    给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
例如，给定一个 3叉树 :
返回其层序遍历:
    [
        [1],
        [3,2,4],
        [5,6]
    ]
说明:
    树的深度不会超过 1000。
    树的节点总数不会超过 5000。

"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        deque = [root]
        res = []
        while deque:
            temp_res, temp_node = [], []
            for node in deque:
                temp_res.append(node.val)
                for child in node.children:
                    temp_node.append(child)
            res.append(temp_res)
            deque = temp_node
        return res
