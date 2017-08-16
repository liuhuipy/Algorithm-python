#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


# Time:  O(m * n)
# Space: O(m * n)

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
#
# Example 1:
#
# Input:
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
#
# Example 2:
#
# Input:
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
# 0 0 0
# 0 1 0
# 1 2 1


class Solution(object):

    def updateMatrix(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        '''
        import collections
        queue = collections.deque([])
        #for python2.x use
        #for i in xrange(len(matrix)
        for i in range(len(matrix)):            #python3.x
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))        #把所有为0的位置（i,j）全部放在一个双向队列中
                else:
                    matrix[i][j] = float('inf')
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            cell = queue.popleft()
            for dir in dirs:
                i, j = cell[0] + dir[0], cell[1] + dir[1]
                #print(matrix[cell[0]][cell[1]])
                if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])) or matrix[i][j] <= matrix[cell[0]][cell[1]]+1:
                    continue
                #print((i,j))
                queue.append((i, j))
                matrix[i][j] = matrix[cell[0]][cell[1]] + 1

        return matrix

if __name__ == "__main__":
    list1 = [
        [0,0,0],
        [0,1,0],
        [1,1,1],
    ]
    solut = Solution()
    list2 = solut.updateMatrix(list1)
    print(list2)
