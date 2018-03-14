#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def ListIsHasNum(self, arr, number):
        h = len(arr)
        w = len(arr[0])
        if number < arr[0][0] or number > arr[h-1][w-1]:
            return False
        for i in range(h):
            if number in arr[i]:
                return True
        return False


if __name__ == '__main__':
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    solut = Solution()
    res = solut.ListIsHasNum(arr, 13)
    print(res)
