#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'liuhui'


class Solution:
    def AllGroupSumIsM(self, n, m):
        if m < 1 or (n * (n + 1) / 2) < m:
            return [[]]
        self.resList = []
        self.SumIsM(n, m, [])

    def SumIsM(self, n, m, s):
        if m < n:
            self.SumIsM(m, m, [])
        if m == n:

            return




if __name__ == '__main__':
    n = int(input())
    m = int(input())
    solut = Solution()
    res = solut.AllGroupSumIsM(n, m)
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j])

