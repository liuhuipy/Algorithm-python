#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
    def reOrderArray(self, array):
        # write code here
        i, num = 0, 1
        while num <= len(array):
            if array[i] % 2 == 0:
                nu = array[i]
                array.remove(array[i])
                array.append(nu)
            else:
                i += 1
            num += 1
        return array


if __name__ == '__main__':
    array = [5,2,9,3,8,4,7,6,12,1,10,11]
    solut = Solution()
    newArray = solut.reOrderArray(array)
    print(newArray)