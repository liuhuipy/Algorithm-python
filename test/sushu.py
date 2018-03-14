#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def isSuShu(self, number):
        if number <= 1:
            return False
        for i in range(2,number):
            pass


if __name__ == '__main__':
    solut = Solution()
    res = solut.isSuShu(7)
    print(res)