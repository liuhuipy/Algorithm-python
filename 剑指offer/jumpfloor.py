#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


class Solution:
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i+1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number+1) % 2]


if __name__ == '__main__':
    solut = Solution()
    res = solut.jumpFloor(10)
    print(res)