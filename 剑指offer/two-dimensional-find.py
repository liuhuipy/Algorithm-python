#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
题目：
    在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个
    二维数组和一个整数，判断数组中是否含有该整数
'''


#从右上角元素开始找，与要查找的元素进行比较，如果等于返回True；如果小于，则去掉该元素所在的行，继续从下一行右上角元素找；
#如果大于，则去掉该元素所在的列，继续从前一列右上角元素找。一直没找到就返回False
class Solution():

    def Find(self, target, array):
        rowCount = len(array)
        colCount = len(array[0])
        if array != None and rowCount > 0 and colCount > 0:
            i = 0
            j = colCount - 1
            while(i<rowCount and j>=0):
                if array[i][j] == target:
                    return True
                elif array[i][j] > target:
                    j -= 1
                else:
                    i += 1
        return False

if __name__ == "__main__":
    array = [
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15],
    ]
    solut = Solution()
    res = solut.Find(5, array)
    print(res)

