#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import sys

class Solution():

    def MaxNum(self, number, cnt):
        maxNum = 0
        for i in range(len(number) - cnt):
            num1 = int(number[0:i] + number[i+cnt:len(number)])
            if num1 > maxNum:
                maxNum = num1
        return maxNum


if __name__ == "__main__":
    number = str(sys.stdin.readline()).strip()
    print(number)
    cnt = int(sys.stdin.readline())
    solut = Solution()
    result = solut.MaxNum(number, cnt)
    print(result)
