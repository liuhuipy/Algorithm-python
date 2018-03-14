#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def InversePairs(self, data):
        # write code here
        if data == []:
            return 0
        resNum = 0
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    resNum += 1
        return resNum % 1000000007


if __name__ == '__main__':
    data = [1, 4, 3, 5, 2, 6, 7, 0]
    solut = Solution()
    resNum = solut.InversePairs(data)
    print(resNum)
