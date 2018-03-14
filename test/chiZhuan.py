#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def ChiZhuanLen(self, m):
        i, k = 0, 0
        while i < len(m) - 1:
            if m[i] == m[i+1]:
                i += 1
                k += 1
            i += 1
        return k

if __name__ == '__main__':
    c = 'RRRRRR'
    solut = Solution()
    res = solut.ChiZhuanLen(c)
    print(res)
