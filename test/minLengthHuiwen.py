#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def minLengthHuiWen(self, s):
        if len(s) == 1:
            return 1
        lens = len(s)
        s2 = []
        for i in range(lens):
            s2.insert(0,s[i])
        if s == s2:
            return lens
        rightLen = 0
        for i in range(lens):
            s = s[1:]
            length = len(s)
            s2 = []
            for i in range(length):
                s2.insert(0, s[i])
            if s == s2:
                rightLen = length
                break
        resLength = (lens - rightLen) * 2 + rightLen
        return resLength

if __name__ == '__main__':
    s = list(sys.stdin.readline().strip())
    solut = Solution()
    resLength = solut.minLengthHuiWen(s)
    print(resLength)