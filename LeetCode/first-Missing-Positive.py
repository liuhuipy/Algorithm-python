#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
            else:
                i += 1
            print(nums)
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    nums = [3, 4, -1, 0, 1]
    solut = Solution()
    res = solut.firstMissingPositive(nums)
    print(res)