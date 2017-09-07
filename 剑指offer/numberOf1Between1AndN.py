#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此
共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
'''

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones


if __name__ == '__main__':
    solut = Solution()
    resN = solut.NumberOf1Between1AndN_Solution(13)
    print(resN)