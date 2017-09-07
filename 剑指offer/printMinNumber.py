#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == None or len(numbers) == 0:
            return ''
        strNum = [str(m) for m in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]
        return ''.join(strNum)


if __name__ == '__main__':
    numbers = [3, 32, 321]
    solut = Solution()
    resNum = solut.PrintMinNumber(numbers)
    print(resNum)