#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
For example, 
Given s = "Hello World",
return 5.
'''

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        last_word = s.split()
        return len(last_word[-1]) if last_word else 0


if __name__ == '__main__':
    s = 'Hello World'
    solut = Solution()
    resNum = solut.lengthOfLastWord(s)
    print(resNum)