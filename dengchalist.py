#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:

    def DengChaList(self, length, initlist):
        if len(initlist) <= 2:
            return 'Possible'
        else:
            for i in range(length):
                for j in range(i+1,length):
                    if initlist[j] < initlist[i]:
                        initlist[i],initlist[j]= initlist[j],initlist[i]

            cha = initlist[1] - initlist[0]
            for i in range(1, length-1):
                if (initlist[i+1] - initlist[i]) != cha:
                    return 'Impossible'
            return 'Possible'


if __name__ == "__main__":


    length = int(sys.stdin.readline().strip())
    initlist = list(map(int, sys.stdin.readline().strip().split()))
    solut = Solution()
    result = solut.DengChaList(length, initlist)
    print(result)
