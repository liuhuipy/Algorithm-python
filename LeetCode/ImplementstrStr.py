#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None or len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1


if __name__ == '__main__':
    haystack = 'a1bc3ed'
    needle = 'c3e'
    solut = Solution()
    res = solut.strStr(haystack, needle)
    print(res)



