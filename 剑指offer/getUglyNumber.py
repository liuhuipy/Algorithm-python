#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == None and len(index) <= 0:
            return 0
        if index <= 0:
            return 0
        uglyNumbers = [1]*index
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextIndex < index:
            minVal = min(uglyNumbers[index2]*2,uglyNumbers[index3]*3,uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal

            while uglyNumbers[index2]*2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 <= uglyNumbers[nextIndex]:
                index5 += 1
            nextIndex += 1

        return uglyNumbers[-1]


    #时间复杂度较高
    '''
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        if index == 1:
            return 1
        self.uglyNumberList = []
        num = 1
        i = 1
        while num <= index-1:
            i += 1
            if self.isUglyNumber(i):
                self.uglyNumberList.append(i)
                num += 1
        return i

    def isUglyNumber(self, number):
        if number == 2 or number == 3 or number == 5:
            return True
        if number in self.uglyNumberList:
            return True
        if number % 2 == 0:
            res = self.isUglyNumber(number // 2)
        elif number % 3 == 0:
            res = self.isUglyNumber(number // 3)
        elif number % 5 == 0:
            res = self.isUglyNumber(number // 5)
        else:
            return False
        return res
    '''


if __name__ == '__main__':
    solut = Solution()
    resNum = solut.GetUglyNumber_Solution(16)
    print(resNum)

