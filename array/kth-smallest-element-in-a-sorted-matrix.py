"""
有序矩阵中第K小的元素：
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素（其中1<=k<=n*n）。
示例：
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],
    k = 8,
    返回 13。
方法1：
    堆维护top k元素。
    时间复杂度为o(n * n)，空间复杂度为O(k)。
方法2：
    二分查找
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        temp_heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(temp_heap) < k:
                    heappush(temp_heap, -matrix[i][j])
                elif temp_heap[0] < -matrix[i][j]:
                    heappush(temp_heap, -matrix[i][j])
                    heappop(temp_heap)
        return -temp_heap[0]


if __name__ == '__main__':
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    matrix_2 = [
        [1, 2],
        [1, 3]
    ]
    print(Solution().kthSmallest(matrix, 8))
