#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
插入排序
'''

class Solution:

    def insert_sort(self, lista):
        for i in range(1, len(lista)):
            mid_num = lista[i]
            j = i - 1
            while j >= 0 and listA[j] > mid_num:
                listA[j+1], listA[j] = listA[j], mid_num
                j -= 1
        return listA


if __name__ == '__main__':
    listA = [3, 1, 5, 8, 6, 7, 4, 2, 10, 9]
    solut = Solution()
    newListA = solut.insert_sort(listA)
    print(newListA)


