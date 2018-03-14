#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def gaiKaoJun(self, n, arr):
        maxNum = max(arr)
        index = arr.index(maxNum)
        arr.remove(arr[index])
        pivot = 0
        for i in arr:
            pivot += i
            if pivot >= maxNum:
                return 'Yes'
        return 'No'


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip().split()
    arr = []
    for j in range(n):
        arr.append(int(s[j]))
    solut = Solution()
    res = solut.gaiKaoJun(n, arr)
    print(res)