#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
            16
      9            18
    6   12      17    25 
   1 7 10 
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        root = sequence[-1]
        index = 0
        for i in range(len(sequence)-1):
            index = i
            if sequence[i] > root:
                break
        for j in range(index+1, len(sequence)-1):
            if sequence[j] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[index:len(sequence)-1])
        return left and right


if __name__ == '__main__':
    array = [1, 7, 6, 10, 12, 9, 17, 25, 18, 16]
    array2 = [1, 7, 6, 10, 12, 9]
    array3 = [6, 12, 9, 16, 17, 25, 28]
    solut = Solution()
    res = solut.VerifySquenceOfBST(array)
    print(res)