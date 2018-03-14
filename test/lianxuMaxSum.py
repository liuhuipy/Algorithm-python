#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import sys


class Solution:

    def MaxSum(self, array):
        if max(array) < 0:
            return max(array)
        global_max, local_max = array[0], 0
        for num in array:
            local_max = max(0, local_max+num)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == '__main__':
    list1 = sys.stdin.readline().strip().split()
    array = []
    for i in range(len(list1)):
        array.append(int(list1[i]))
    solut = Solution()
    res = solut.MaxSum(array)
    print(res)