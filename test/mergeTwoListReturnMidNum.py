#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def MergeTwoListReturnMidNum(self, s1, n, s2, m):
        resList = self.MergeSort(s1, n, s2, m)
        print(resList)
        length = len(resList)
        if length % 2 == 0:
            if (resList[length // 2 - 1] + resList[length // 2]) % 2 != 0:
                midNum = (resList[length // 2 - 1] + resList[length // 2]) / 2 + 0.5
            else:
                midNum = (resList[length // 2 - 1] + resList[length // 2]) / 2 + 0.0
        else:
            midNum = resList[length // 2] + 0.0
        return midNum

    def MergeSort(self, s1, n, s2, m):
        if n == 0:
            return s2
        if m == 0:
            return s1
        resList = []
        l, r = 0, 0
        while l < n and r < m:
            if s1[l] < s2[r]:
                resList.append(s1[l])
                l += 1
            elif s1[l] > s2[r]:
                resList.append(s2[r])
                r += 1
            else:
                resList.append(s1[l])
                resList.append(s2[r])
                l += 1
                r += 1
        if l < n:
            resList.extend(s1[l:])
        if r < m:
            resList.extend(s2[r:])
        return resList


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    s1 = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline())
    s2 = list(map(int, sys.stdin.readline().strip().split()))
    solut = Solution()
    resNum = solut.MergeTwoListReturnMidNum(s1, n, s2, m)
    print(resNum)

