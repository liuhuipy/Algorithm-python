#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def GetMinNumForRemoveKNum(self, num, K):
        length = len(num)
        if length == K:
            return 0
        resLen = length - K
        resNum = int(num)
        for i in range(resLen+1):
            if i == 0:
                temp = num[i+K:]
            elif i == resLen:
                temp = num[:i]
            else:
                temp = num[:i] + num[i+K:]
            if int(temp) < resNum:
                resNum = int(temp)
        return resNum



if __name__ == '__main__':
    num = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    solut = Solution()
    resNum = solut.GetMinNumForRemoveKNum(num, K)
    print(resNum)
