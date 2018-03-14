#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def PrintJiEZhi(self, n, m, nums, arr):
        nums.sort()
        temp = []
        for i,item in enumerate(arr):
            temp.append(item)
        temp.sort()
        res = []
        for j in range(n - 1, -1, -1):
            k = m - 1
            Zhi = arr[temp[j]]
            while k >= 0:
                if nums[k] <= Zhi:
                    Zhi -= nums[k]
                    nums.remove(nums[k])
                    m -= 1
                    k -= 1
                else:
                    k -= 1
            res.append(Zhi)
        return res


if __name__ == "__main__":
    s = sys.stdin.readline().strip().split()
    nums = list(map(int,sys.stdin.readline().strip().split()))
    n, m = int(s[0]), int(s[1])
    arr = {}
    for i in range(n):
        a = sys.stdin.readline().strip().split()
        arr[int(a[0])] = int(a[1])
    solut = Solution()
    res = solut.PrintJiEZhi(n, m, nums, arr)
    for i in range(len(res)):
        print(res[i])

