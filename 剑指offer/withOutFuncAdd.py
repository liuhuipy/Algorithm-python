#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
实现一个函数，计算两个数加法，不能使用+,-,*,/
'''

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp
        return num1

    def Add2(self, num1, num2):
        if num1 & num2:
            return self.Add2((num1 & num2)<<1, num1 ^ num2)
        else:
            return num1 ^ num2

if __name__ == '__main__':
    solut = Solution()
    res = solut.Add2(123,54)
    print(res)
