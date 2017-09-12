#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        i, n = 0, len(nums)
        while i < n and n > 0:
            if nums[i] == val:
                nums.remove(nums[i])
                n -= 1
            else:
                i += 1
        return n

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    solut = Solution()
    res = solut.removeElement(nums, 3)
    print(res)
