#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def IsIpv4(self, ip):
        if len(ip) < 7 or ip[0] == '.' or ip[-1] == '.':
            return 0
        ipList = list(map(int, ip.strip().split(".")))
        print(ipList)
        if len(ipList) != 4:
            return 0
        for i, num in enumerate(ipList):
            if i == 4:
                if num < 0 or num > 254:
                    return 0
            if num < 0 or num > 255:
                return 0
        return 1

if __name__ == '__main__':
    ip = sys.stdin.readline()
    solut = Solution()
    res = solut.IsIpv4(ip)
    print(res)
