#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
      5               3
   3     8          6   1
 6   1 7   2           4 
    4 
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot2 == None or pRoot1 == None :
            return res
        if pRoot1.val == pRoot2.val:
            res = self.isSameTree(pRoot1, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)

        return res

    def isSameTree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSameTree(pRoot1.left, pRoot2.left) and self.isSameTree(pRoot1.right, pRoot2.right)



if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(8)
    node4 = TreeNode(6)
    node5 = TreeNode(1)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8

    pnode1 = TreeNode(3)
    pnode2 = TreeNode(6)
    pnode3 = TreeNode(1)
    pnode4 = TreeNode(4)
    pnode1.left = pnode2
    pnode1.right = pnode3
    pnode3.left = pnode4

    solut = Solution()
    res = solut.HasSubtree(node1, pnode1)
    print(res)

