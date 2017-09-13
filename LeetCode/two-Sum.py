#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        dic = {}
        for i, item in enumerate(nums):
            if (target - item) in dic:
                return [dic[target - item], i]
            dic[item] = i
        return []

if __name__ == '__main__':
    nums = [2, 7, 7, 11, 15]
    solut = Solution()
    res = solut.twoSum(nums, 9)
    print(res)
