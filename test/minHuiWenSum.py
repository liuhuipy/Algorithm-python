#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def MinHuiWenSum(self, n, arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return 2 * arr[0]
        l = r = len(arr) // 2 - 1
        while l < r:
            if arr[l] != arr[r]:
                pass
            else:
                l += 1
                r -= 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    solut = Solution()
    resSum = solut.MinHuiWenSum(n, arr)
    print(resSum)
