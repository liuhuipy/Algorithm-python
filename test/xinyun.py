#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:

    def luckyNum(self, n):
        number = 0
        for i in range(1, n+1):
            strn = str(i)
            fn = 0
            for j in range(len(strn)):
                fn += int(strn[j])
            xn = 0
            while i >= 2:
                a = i % 2
                i //= 2
                xn += a
            xn += i
            if xn == fn:
                number += 1
        return number



if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    solut = Solution()
    res = solut.luckyNum(n)
    print(res)