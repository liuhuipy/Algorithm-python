#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return -1
        adict = {}
        alist = list(s)
        for i in alist:
            if i not in adict.keys():
                adict[i] = 0
            adict[i] += 1
        for i in alist:
            if adict[i] == 1:
                return alist.index(i)
        return -1


if __name__ == '__main__':
    s = 'dabaacdbcaefgf'
    solut = Solution()
    resStr = solut.FirstNotRepeatingChar(s)
    print(resStr)
