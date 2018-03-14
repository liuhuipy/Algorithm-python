#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def quicksort(self, alist, left, right):
        if left >= right:
            return alist
        key = alist[left]
        low = left
        high = right
        while left < right:
            while left < right and alist[right] >= key:
                right -= 1
            alist[left] = alist[right]
            while left < right and alist[left] <= key:
                left += 1
            alist[right] = alist[left]
        alist[right] = key
        #print(alist)
        self.quicksort(alist, low, left - 1)
        self.quicksort(alist, left + 1, high)
        return alist


if __name__ == '__main__':
    alist = [3,1,5,4,6,7,2,8]
    solut = Solution()
    resList = solut.quicksort(alist, 0, len(alist) - 1)
    print(resList)
