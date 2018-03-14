#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:

    def __init__(self):
        self.stac = []
        self.cmp = []

    def push(self, node):
        self.stac.append(node)
        if self.cmp == []:
            self.cmp.append(node)
        else:
            if self.cmp[-1] > node:
                self.cmp.append(node)
            if self.cmp[-1] <= node:
                tmp = self.cmp[-1]
                self.cmp.append(tmp)

solut = Solution()
solut.push(4)