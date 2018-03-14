#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class LongestDistance:
    def getDis(self, A, n):
        # write code here
        min = A[0]
        maxCha = 0
        for i in range(1,n):
            if A[i] < min:
                min = A[i]
            cha = A[i] - min
            if cha > maxCha:
                maxCha = cha
        return maxCha


if __name__ == '__main__':
    A = [3,1,6,2,4,10,7,12,6,8,11,5]
    p = LongestDistance()
    res = p.getDis(A,len(A))
    print(res)