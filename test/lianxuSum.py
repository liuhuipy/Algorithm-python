#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def LianXuMaxSum(self, arr, n):
        if max(arr) < 0:
            return max(arr)
        maxNum, local_max = arr[0], 0
        for num in arr:
            local_max = max(0, local_max+num)
            maxNum = max(maxNum, local_max)
        return maxNum

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    solut = Solution()
    resNum = solut.LianXuMaxSum(arr, n)
    print(resNum)
