#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [-2,1,4,-2,2,3], k = 3
Output: 3
'''

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = s = 0
        sums = {0: 1}
        for n in nums:
            s += n
            res += sums.get(s - k, 0)
            sums[s] = sums.get(s, 0) + 1
        return res


if __name__ == '__main__':
    nums = [-2,1,4,-2,2,3]
    solut = Solution()
    res = solut.subarraySum(nums, 3)
    print(res)
