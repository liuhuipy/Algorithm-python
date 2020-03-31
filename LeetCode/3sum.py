#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        n = len(nums)
        resList = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp + nums[i] == 0:
                    resList.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif tmp + nums[i] < 0:
                    l += 1
                else:
                    r -= 1
        return resList


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    num1 = [0, 0, 0]
    solut = Solution()
    res = solut.threeSum(nums)
    print(res)
