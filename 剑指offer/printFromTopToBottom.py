#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
        1
    2       3
  4   5   6   7      ---->    [1,2,3,4,5,6,7,8]
     8  
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1, 2, 3]
    def PrintFromTopToBottom(self, root):
        # write code here
        queue = []
        if root is None:
            return []
        resList = []
        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            resList.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return resList

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8

    solut = Solution()
    resList = solut.PrintFromTopToBottom(node1)
    print(resList)
