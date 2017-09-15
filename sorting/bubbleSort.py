#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
冒泡排序
'''

class Solution:
    def BubbleSort(self, alist):
        for i in range(len(alist)-1):
            for j in range(1, len(alist)):
                if alist[j-1] > alist[j]:
                    alist[j-1], alist[j] = alist[j], alist[j-1]
        return alist


if __name__ == '__main__':
    alist = [8, 7, 6, 5, 4, 3, 2, 1]
    solut = Solution()
    res = solut.BubbleSort(alist)
    print(res)
