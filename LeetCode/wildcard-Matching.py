#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


'''
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        sstar = 0
        star = -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                sstar = i
            elif star != -1:
                j = star + 1
                sstar += 1
                i = sstar
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        if j == len(p):
            return True
        return False


if __name__ == '__main__':
    s1, p1 = 'ab', '?*'
    s2, p2 = 'aab', 'c*a*b'
    s3, p3 = 'aa', 'a*'
    s, p = "abefcdgiescdfimde", "ab*cd?i*de"
    solut = Solution()
    res = solut.isMatch(s, p)
    print(res)