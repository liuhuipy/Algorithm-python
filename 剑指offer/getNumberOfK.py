#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
统计一个数字在排序数组中出现的次数。
'''

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if k not in data:
            return 0
        adict = {}
        for i in data:
            if i not in adict.keys():
                adict[i] = 0
            adict[i] += 1
        return adict[k]
    # 方法2,二分法查找出第一次出现k的位置和最后一次出现k的位置，即可算出k在data数组中出现的次数
    def GetNumberOfK2(self, data, k):
        if k not in data:
            return 0
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            kIndex = self.GetIndexK(data, length, k, 0, length-1)
            first, last = kIndex, kIndex
            while first > 0 and data[first - 1] == k:
                first -= 1
            while last < length-1 and data[last + 1] == k:
                last += 1
            number = last - first + 1
        return number

    def GetIndexK(self, data, length, k, start, end):
        if start > end:
            return -1
        midIndex = (start + end) // 2
        midData = data[midIndex]

        if midData == k:
            return midIndex
        elif midData > k:
            end = midIndex - 1
        else:
            start = midIndex + 1
        return self.GetIndexK(data, length, k, start, end)

if __name__ == '__main__':
    data = [1,2,2,3,4,4,4,5,6,6,6,6,6,7,7,8]
    solut = Solution()
    resNum = solut.GetNumberOfK2(data, 6)
    print(resNum)
