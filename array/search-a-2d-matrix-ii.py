"""
搜索二维矩阵II:
    编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
示例:
    现有矩阵 matrix 如下：
    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
方法：
    利用每行的元素从左到右升序排列，每列的元素从上到下升序排列。只需从矩阵右上角matrix[row][col]开始查找，如果当前指向的值大于目标值，
    则col减1；如果当前指向的值小于目标值，则row加1；直到指向的值与目标值相等或者row、col以达到边界。
    时间复杂度为O(m+n)，空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        len_row, len_col = len(matrix), len(matrix[0])
        col, row = len_col - 1, 0
        while col >= 0 and row < len_row:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

