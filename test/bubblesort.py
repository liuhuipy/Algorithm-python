#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def BubbleSort(self, arr, n):
        if n <= 1:
            return arr
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
        return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    solut = Solution()
    resArr = solut.BubbleSort(arr, n)
    res = ' '.join(str(i) for i in resArr)
    print(res)
