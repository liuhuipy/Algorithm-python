#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 2**31 - 1
        length = len(nums)
        if length < 3:
            return result
        nums.sort()
        larger_count = 0
        for i, item_i in enumerate(nums):
            l, r = i+1, length - 1
            if l < r:
                sum3_smallest = nums[l] + nums[l+1] + item_i
                if sum3_smallest > target:
                    larger_count += 1
                    if larger_count > 1:
                        return result

            while l < r:
                sum3 = nums[l] + nums[r] + item_i
                if abs(sum3 - target) < abs(result - target):
                    result = sum3

                sum_flag = 0
                if sum3 > target:
                    r -= 1
                    if sum_flag == -1:
                        break
                    sum_flag = 1
                elif sum3 < target:
                    l += 1
                    if sum_flag == 1:
                        break
                    sum_flag = -1
                else:
                    return result
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    solut = Solution()
    res = solut.threeSumClosest(nums, 1)
    print(res)