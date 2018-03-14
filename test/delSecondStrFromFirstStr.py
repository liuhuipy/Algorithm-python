#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def DelSecondStrFromFirstStr(self, str1, str2):
        resStr = ''
        for i in range(len(str1)):
            if str1[i] not in str2:
                resStr += str1[i]
        return resStr

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    solut = Solution()
    resStr = solut.DelSecondStrFromFirstStr(str1, str2)
    print(resStr)
