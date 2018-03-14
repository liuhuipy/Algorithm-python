#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def AllIp(self, ip):
        if len(ip) < 4 or len(ip) > 12:
            return []
        self.res = []
        self.ChoiceIp(ip, 4, '')

    def ChoiceIp(self, ip, n, s):
        if n == 1 and int(ip) > 0 and int(ip) < 255:
            return
        if len(ip) / n > 3:
            return
        l, newIp = 1, ip[1:]
        if self.ChoiceIp(newIp, n - 1):
            s += 1


if __name__ == '__main__':
    ip = sys.stdin.readline()
    solut = Solution()
    res = solut.AllIp(ip)
    print(res)
