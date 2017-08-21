#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

class Solution:
    def jumpFloorII(self, number):
        # write code here
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans


if __name__ == '__main__':
    solut = Solution()
    res = solut.jumpFloorII(10)
    print(res)
