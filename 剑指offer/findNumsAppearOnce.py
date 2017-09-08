#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) <= 1:
            return array
        adict = {}
        resList = []
        for i in array:
            if i not in adict.keys():
                adict[i] = 0
            adict[i] += 1
        for i in adict.keys():
            if adict[i] == 1:
                resList.append(i)
        return resList


if __name__ == '__main__':
    array = [1,4,2,2,3,1,1,5,6,3,]
    solut = Solution()
    resList = solut.FindNumsAppearOnce(array)
    print(resList)

