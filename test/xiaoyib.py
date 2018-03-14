#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def reverseBlist(self, n, alist):
        for i in range(n-1, -1, -2):
            print(alist[i],)
        if n%2 != 0:
            for j in range(1,n,2):
                print(alist[j],)
        else:
            for j in range(0, n, 2):
                print(alist[j],)



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    alist = list(map(int, sys.stdin.readline().strip().split()))
    solut = Solution()
    solut.reverseBlist(n, alist)

