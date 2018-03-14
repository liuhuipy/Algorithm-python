#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def __init__(self):
        self.whiteList = {}

    def Add(self, s):
        length = len(self.whiteList)
        self.whiteList[s] = 1
        if len(self.whiteList) == length + 1 and self.whiteList[s]:
            return True
        else:
            return False

    def Del(self, s):
        if s not in self.whiteList or self.whiteList[s] == 0:
            return False
        else:
            self.whiteList[s] = 0
            return True

    def Search(self, s):
        if s in self.whiteList and self.whiteList[s] >= 1:
            return True
        else:
            return False



if __name__ == '__main__':
    solut = Solution()
    res = []
    while True:
        s = sys.stdin.readline().strip()
        if s == 'end':
            break
        s = s.split(':')
        if s[0] == 'i':
            if solut.Add(s[1]):
                res.append('ok')
        if s[0] == 'd':
            if solut.Del(s[1]):
                res.append('ok')
        if s[0] == 's':
            if solut.Search(s[1]):
                res.append('true')
            else:
                res.append('false')
    for i, s in enumerate(res):
        print(s)

