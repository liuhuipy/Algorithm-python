#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def __init__(self):
        self.arr = {}
        self.temp = {}
        self.mkssList = {}
        self.res = []

    def put(self, key, value):
        self.arr[key] = value
        self.temp[key] = value

    def mkss(self, ssid):
        self.mkssList[ssid] = self.temp
        self.temp = {}

    def delKey(self, key):
        self.arr.pop(key)

    def get(self, key, ssid=''):
        if ssid == '':
            if key not in self.arr:
                self.res.append('(NULL)')
            else:
                self.res.append(self.arr[key])
        else:
            if ssid not in self.mkssList:
                self.res.append('(UNKNOWN_SSID)')
            else:
                if key not in self.mkssList[ssid]:
                    self.res.append('(NULL)')
                else:
                    self.res.append(self.mkssList[ssid][key])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    solut = Solution()
    for i in range(n):
        s = sys.stdin.readline().strip().split()
        if s[0] == 'put':
            solut.put(s[1], s[2])
        if s[0] == 'mkss':
            solut.mkss(s[1])
        if s[0] == 'del':
            solut.delKey(s[1])
        if s[0] == 'get':
            if len(s) == 3:
                solut.get(s[1],s[2])
            else:
                solut.get(s[1])
    res = solut.res
    for i in range(len(res)):
        print(res[i])
