#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def MaxYingBi(self, n):
        if n == 1:
            return [1, 1]
        tes = [1,3,8,18,38,88,188]

        typeNum,resNum = 0,0
        for i in range(len(tes)):
            if tes[i] > n:
                typeNum = i
                resNum = i + (n-tes[i-1])
        return [typeNum,resNum]

if __name__ == '__main__':
    n = int(input())
    solut = Solution()
    res = solut.MaxYingBi(n)
    print(res[0],res[1])
