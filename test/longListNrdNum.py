#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

class Solution:
    def longListNrdNum(self, n):
        if n < 1:
            return 0
        i = 1
        while True:
            if (1 + i) * i // 2 >= n:
                return i
            i += 1

if __name__ == '__main__':
    n = int(input())
    solut = Solution()
    resNum = solut.longListNrdNum(n)
    print(resNum)