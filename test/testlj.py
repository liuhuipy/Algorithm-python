#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import sys

class Solution:

    def MaxNumAdd(self, m, n, k, array):
        left = m - (n * k - 1)
        maxNum = 0
        for i in range(left + 1):
            right = i + n * k - 1
            number = 0
            for j in range(i, right, k):
                number += array[j]
            if maxNum < number:
                maxNum = number
        return maxNum

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip().split()
    line2 = sys.stdin.readline().strip().split()
    array = []
    for i in line2:
        array.append(int(i))
    m = int(line1[0])
    n = int(line1[1])
    k = int(line1[2])
    solut = Solution()
    maxNum = solut.MaxNumAdd(m, n, k, array)
    print(maxNum)