#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
            1
       2         3  
    4     5   6     7    ----->   深度为4
     8
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法1，递归，每次返回左右子树深度的最大值
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        lDepth = self.TreeDepth(pRoot.left)
        rDepth = self.TreeDepth(pRoot.right)
        return max(lDepth, rDepth) + 1

if __name__ == '__main__':
    pnode1 = TreeNode(1)
    pnode2 = TreeNode(2)
    pnode3 = TreeNode(3)
    pnode4 = TreeNode(4)
    pnode5 = TreeNode(5)
    pnode6 = TreeNode(6)
    pnode7 = TreeNode(7)
    pnode8 = TreeNode(8)
    pnode1.left = pnode2
    pnode1.right = pnode3
    pnode2.left = pnode4
    pnode2.right = pnode5
    pnode3.left = pnode6
    pnode3.right = pnode7
    pnode4.right = pnode8

    solut = Solution()
    resTreeDepth = solut.TreeDepth(pnode1)
    print(resTreeDepth)


