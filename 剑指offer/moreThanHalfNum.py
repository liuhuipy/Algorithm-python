#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


# 方法一：先将数组排序，数组有一个数字出现的次数超过数组长度一半的数必定在数组中间位置。再判断这个数字长度是否超过一半
class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 1:
            return numbers[0]
        numbers = self.quickSort(numbers)
        mid = (len(numbers)+1) // 2 - 1
        midNum = numbers[mid]
        resNum = 0
        for i in range(mid,-1,-1):
            if numbers[i] == midNum:
                resNum += 1
            else:
                break
        for j in range(mid+1,len(numbers)+1):
            if numbers[j] == midNum:
                resNum += 1
            else:
                break
        if resNum > len(numbers)//2:
            return midNum
        else:
            return 0

    def quickSort(self, numbers):
        if len(numbers) <= 1:
            return numbers
        pivot = numbers[0]
        return self.quickSort([i for i in numbers[1:] if i <= pivot]) + [pivot] + self.quickSort([j for j in numbers[1:] if j > pivot])


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solut = Solution()
    result = solut.MoreThanHalfNum_Solution(numbers)
    print(result)