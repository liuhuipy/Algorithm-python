#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        front, rear, midIndex = 0, len(rotateArray) - 1, 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.MininOrder(rotateArray, front, rear)
            if rotateArray[midIndex] >= rotateArray[front]:
                front = midIndex
            elif rotateArray[midIndex] <= rotateArray[rear]:
                rear = midIndex
        return rotateArray[midIndex]

    def MininOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end+1]:
            if i < result:
                result = i
        return result


if __name__ == '__main__':
    array1 = [3, 4, 5, 1, 2]
    solut = Solution()
    result = solut.minNumberInRotateArray(array1)
    print(result)
