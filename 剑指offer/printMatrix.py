#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) <= 1:
            return matrix[0]

        resList = matrix[0]
        matrix.remove(matrix[0])
        choices = [(0,1),(-1,0),(0,-1),(1,0)]
        i = 0
        while matrix != []:

            rotate = choices[i % 4]

            if rotate == (0, 1):
                Index = len(matrix[0]) - 1
                for j in range(len(matrix)):
                    resList.append(matrix[j][Index])
                    del(matrix[j][Index])
                if matrix[0] == []:
                    for j in range(len(matrix)):
                        matrix.remove(matrix[0])

            elif rotate == (-1, 0):
                Index = len(matrix) - 1
                for k in range(len(matrix[0])-1,-1,-1):
                    resList.append(matrix[Index][k])
                matrix.remove(matrix[Index])

            elif rotate == (0, -1):
                Index = len(matrix) - 1
                for m in range(Index,-1,-1):
                    resList.append(matrix[m][0])
                    del(matrix[m][0])
                if matrix[0] == []:
                    for j in range(len(matrix)):
                        matrix.remove(matrix[0])
            else:
                for n in range(len(matrix[0])):
                    resList.append(matrix[0][n])
                matrix.remove(matrix[0])
            i += 1
        return resList



if __name__ == '__main__':
    array = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    array1 = [[1]]
    array2= [[1],[2],[3],[4],[5]]
    array3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    solut = Solution()
    newList = solut.printMatrix(array2)
    print(newList)


