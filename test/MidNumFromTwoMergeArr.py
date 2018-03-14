#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def GetMidNumFromTwoMergeArr(self, list1, list2):
        resList = self.MergeTwoList(list1, list2)
        length = len(resList)
        if length % 2 == 0:
            tem = resList[length // 2 - 1] + resList[length // 2]
            if tem % 2 == 0:
                midNum = tem // 2
            else:
                midNum = tem / 2
        else:
            midNum = resList[length // 2]
        return midNum

    def MergeTwoList(self, list1, list2):
        m, n = len(list1), len(list2)
        if m == 0:
            return list2
        if n == 0:
            return list1
        resList = []
        l, r = 0, 0
        while l < m and r < n:
            if list1[l] < list2[r]:
                resList.append(list1[l])
                l += 1
            elif list1[l] > list2[r]:
                resList.append(list2[r])
                r += 1
            else:
                resList.append(list1[l])
                resList.append(list2[r])
                l += 1
                r += 1
        if l < m:
            resList.extend(list1[l:])
        if r < n:
            resList.extend(list2[r:])
        return resList


if __name__ == '__main__':
    list1 = list(map(int, sys.stdin.readline().strip().split(',')))
    list2 = list(map(int, sys.stdin.readline().strip().split(',')))
    solut = Solution()
    midNum = solut.GetMidNumFromTwoMergeArr(list1, list2)
    print(midNum)