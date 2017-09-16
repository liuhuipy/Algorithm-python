#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums)
        appearTime = 1
        while l < r:
            if nums[l] == nums[l-1]:
                if appearTime >= 2:
                    nums.remove(nums[l])
                    r -= 1
                else:
                    appearTime += 1
                    l += 1
            else:
                appearTime = 1
                l += 1
        return r


if __name__ == '__main__':
    nums = [1,1,1,1,2,2,2,3,3,4]
    solut = Solution()
    resLen = solut.removeDuplicates(nums)
    print(resLen)
