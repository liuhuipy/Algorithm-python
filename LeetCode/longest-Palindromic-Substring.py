#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''

#O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        res = ''
        for i in range(len(s)):
            t = self.palindrome(s, i, i)
            if len(t) > len(res):
                res = t
            t = self.palindrome(s, i, i + 1)
            if len(t) > len(res):
                res = t
        return res

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


#O(n^3)
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n = len(s)
        longest, l, r = 0, 0, 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if self.isPalindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    l, r = i, j
        return s[l:r]

    def isPalindrome(self, s):
        if not s:
            return False
        return s == s[::-1]


if __name__ == '__main__':
    s = 'babad'
    s1 = 'abcbe'
    solut = Solution()
    res = solut.longestPalindrome(s)
    print(res)