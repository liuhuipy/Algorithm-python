#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def AixAi1Is4(self, array, n):
        if n == 1:
            if array[0] % 4 == 0:
                return 'Yes'
            return 'No'
        index4, index1 = 0, 0
        for i in range(n):
            if array[i] % 4 == 0:
                index4 += 1
            elif array[i] % 2 != 0:
                index1 += 1
        if index4 >= index1:
            return 'Yes'
        else:
            return 'No'

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    resList = []
    for i in range(t):
        n = int(sys.stdin.readline())
        array = list(map(int, sys.stdin.readline().strip().split()))
        solut = Solution()
        resList.append(solut.AixAi1Is4(array, n))
    for i in range(t):
        print(resList[i])
