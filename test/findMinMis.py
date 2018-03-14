#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def FindMinMis(self, A):
        length = len(A)
        tes = []
        for i in range(length):
            tes.append(0)
        for i in range(length):
            if A[i] <= length and A[i] > 0:
                tes[A[i]-1] = A[i]
        for i, item in enumerate(tes):
            if item == 0:
                return i + 1
        return length + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = []
    for i in range(n):
        A.append(int(sys.stdin.readline()))
    solut = Solution()
    resNum = solut.FindMinMis(A)
    print(resNum)

