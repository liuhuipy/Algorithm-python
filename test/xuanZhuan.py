#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys
from math import fabs

class Solution:
    def xuanZhuan(self, n1, n2):
        if n1 <= n2:
            if n2 - n1 >= 180:
                return -(360 - n2 + n1)
            return n2 - n1
        else:
            if n1 - n2 >= 180:
                return 360 - n1 + n2
            return -(n1 - n2)

if __name__ == '__main__':
    n1 = int(sys.stdin.readline().strip())
    n2 = int(sys.stdin.readline().strip())
    solut = Solution()
    res = solut.xuanZhuan(n1, n2)
    print(res)
