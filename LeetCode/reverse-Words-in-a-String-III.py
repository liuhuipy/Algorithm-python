#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        lis = s.strip().split()
        resStr = lis[0][::-1]
        for stri in lis[1:]:
            stri = ' ' + stri[::-1]
            resStr += stri
        return resStr

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solut = Solution()
    resStr = solut.reverseWords(s)
    print(resStr)


