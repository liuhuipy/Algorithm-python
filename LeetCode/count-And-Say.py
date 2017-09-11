#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        s = self.countAndSay(n-1)
        mstr, resStr, num = s[0], '', 1
        for i in range(1, len(s)):
            if s[i] != mstr:
                sStr = str(num) + s[i-1]
                resStr += sStr
                mstr = s[i]
                num = 1
            else:
                num += 1
        sStr = str(num) + s[-1]
        resStr += sStr
        return resStr

if __name__ == '__main__':
    solut = Solution()
    resStr = solut.countAndSay(5)
    print(resStr)
