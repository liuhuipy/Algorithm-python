#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def DelStr(self, s):
        if len(s) <= 1:
            return s
        temp, resStr = {}, ''
        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = 1
                resStr += s[i]
        return resStr

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    solut = Solution()
    resStr = solut.DelStr(s)
    print(resStr)
