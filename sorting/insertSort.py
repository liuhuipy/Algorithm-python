#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
插入排序
'''

class Solution:

    def insertSort(self, listA):
        for i in range(1, len(listA)):
            midNum = listA[i]
            j = i - 1
            while j >= 0 and listA[j] > midNum:
                listA[j+1], listA[j] = listA[j], midNum
                j -= 1
        return listA


if __name__ == '__main__':
    listA = [3, 1, 5, 8, 6, 7, 4, 2, 10, 9]
    solut = Solution()
    newListA = solut.insertSort(listA)
    print(newListA)


