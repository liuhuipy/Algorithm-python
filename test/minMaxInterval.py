#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def MinMaxInterval(self, n, array):
        if n <= 1:
            return None
        if n == 2:
            return array[1] - array[0]

        resMin = array[-1] - array[0]
        for i in range(1, n-1):
            resList = array
            resList.remove(resList[i])
            print(resList)
            resMax = 0
            for j in range(n-2):
                cha = resList[j+1] - resList[j]
                if cha > resMax:
                    resMax = cha
            if resMax < resMin:
                resMin = resMax
        return resMin

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    solut = Solution()
    resMin = solut.MinMaxInterval(n, array)
    print(resMin)