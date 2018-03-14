#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def ReverseNum(self, number):
        numberL = list(str(number))
        while numberL[-1] == '0':
            numberL.pop()
        length = len(numberL)
        reverseNum = ''
        for i in range(length-1,-1,-1):
            reverseNum += numberL[i]

        reverseNum = int(reverseNum)
        resNum = reverseNum + number
        return resNum


if __name__ == '__main__':
    number = int(input())
    solut = Solution()
    resNum = solut.ReverseNum(number)
    print(resNum)