#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

if __name__ == '__main__':
    list1 = []
    while True:
        line = sys.stdin.readline().strip().split()
        if not line:
            break
        list1.append(int(line[0])+int(line[1]))
    for i in range(len(list1)):
        print(list1[i])
