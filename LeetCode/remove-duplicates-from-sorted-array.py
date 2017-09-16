#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums)
        while l < r:
            if nums[l] == nums[l-1]:
                nums.remove(nums[l])
                r -= 1
            else:
                l += 1
        return r

if __name__ == '__main__':
    nums = [1,1,2,2,3,3,3,5,6,6,7]
    solut = Solution()
    resLen = solut.removeDuplicates(nums)
    print(resLen)
