#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''


class Solution:

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2 or tsum < array[0]+array[1] or tsum > array[len(array)-1] + array[len(array)-2]:
            return []
        left, right = 0, len(array) -1
        self.minN = array[len(array) - 1]
        self.FindSum(left, right, array, tsum)
        if self.minN < array[len(array) -1]:
            maxN = tsum - self.minN
            return [self.minN, maxN]
        else:
            return []

    def FindSum(self, left, right, array, tsum):
        if left == right:
            return
        if array[left] + array[right] < tsum:
            self.FindSum(left+1, right, array, tsum)
        elif array[left] + array[right] > tsum:
            self.FindSum(left, right-1, array, tsum)
        else:
            if array[left] < self.minN:
                self.minN = array[left]
            return


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    array = []
    solut = Solution()
    res = solut.FindNumbersWithSum(array, 0)
    print(res)