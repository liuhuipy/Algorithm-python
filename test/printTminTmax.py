#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def PrintTminTmax(self, n, k, arr):
        if k > n:
            return 'error'
        length = len(arr)
        Tmin, Tmax = 50, -50
        for i in range(length):
            minTemp, maxTemp = arr[i][0], arr[i][1]
            Mink, Maxk = 0, 0
            for j in range(length):
                if minTemp in range(arr[j][0], arr[j][1] + 1):
                    Mink += 1
                if maxTemp in range(arr[j][0], arr[j][1] + 1):
                    Maxk += 1
            if Mink >= k and minTemp < Tmin:
                Tmin = minTemp
            if Maxk >= k and maxTemp > Tmax:
                Tmax = maxTemp
        if Tmin == 50 and Tmax == -50:
            return 'error'
        res = str(Tmin) + ' ' + str(Tmax)
        return res


if __name__ == "__main__":
    s = sys.stdin.readline().strip().split()
    n, k = int(s[0]), int(s[1])
    arr = []
    for i in range(n):
        a = sys.stdin.readline().strip().split()
        arr.append([int(a[0]), int(a[1])])
    solut = Solution()
    res = solut.PrintTminTmax(n, k, arr)
    print(res)