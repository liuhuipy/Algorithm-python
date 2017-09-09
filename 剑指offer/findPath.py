#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往
下一直到叶结点所经过的结点形成一条路径。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.resList = []
        self.FindChildPath(root, expectNumber,[])
        return self.resList

    def FindChildPath(self, root, expectNumber,luJing):
        luJing += [root]
        if root is None:
            return
        if root.val > expectNumber:
            return
        if root.val == expectNumber:
            print(root.val)
            self.resList.append(luJing)

        expectNumber -= root.val
        lNode = self.FindChildPath(root.left, expectNumber,luJing)
        rNode = self.FindChildPath(root.right, expectNumber,luJing)


if __name__ == '__main__':
    pnode1 = TreeNode(1)
    pnode2 = TreeNode(2)
    pnode3 = TreeNode(3)
    pnode4 = TreeNode(4)
    pnode5 = TreeNode(5)
    pnode6 = TreeNode(6)
    pnode7 = TreeNode(7)
    pnode1.left = pnode2
    pnode1.right = pnode3
    pnode2.left = pnode7
    pnode2.right = pnode5
    pnode3.left = pnode4
    pnode3.right = pnode6

    solut = Solution()
    resList = solut.FindPath(pnode1,8)
    print(resList)
    for i in range(len(resList)):
        for j in range(len(resList[i])):
            print(resList[i][j].val)
