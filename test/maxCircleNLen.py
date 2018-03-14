#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def maxCircleNLen(self, n, array):
        if n<2:
            return 0
        array = self.quickSort(array)
        for i in range(n):
            array.append(array[i]+360.00000000)
        minN, maxN = array[0], array[-1]
        if maxN - minN <= 180:
            return maxN - minN

        maxL = 0
        for i in range(2*n-1):
            pivot = array[i] + 180
            if pivot >= maxN:
                maxMid = maxN - array[i]
                if maxMid > maxL:
                    maxL = maxMid
                    continue
            else:
                for j in range(i+1, 2*n):
                    if array[j] <= pivot:
                        pass
                    else:
                        maxMid = array[j-1] - array[i]
                        if maxMid > maxL:
                            maxL = maxMid
                        break

        return maxL

    def quickSort(self, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        return self.quickSort([i for i in array[1:] if i <= pivot]) + [pivot] + self.quickSort([j for j in array[1:] if j > pivot])

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    array = []
    for i in range(n):
        array.append(float(sys.stdin.readline().strip()))
    solut = Solution()
    maxL = solut.maxCircleNLen(n, array)
    print(maxL)

