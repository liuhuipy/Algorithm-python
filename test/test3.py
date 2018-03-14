#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:

    def fibonacci(self, n):
        tempArray = [0,1]
        for i in range(2, n+1):
            tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]


if __name__ == '__main__':
    number = int(sys.stdin.readline().strip())
    solut = Solution()
    res = solut.fibonacci(number)
    print(res)
