#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import sys

s = set()
while True:
    line = sys.stdin.readline()
    if not line.strip():
        break
    for i in line.split():
        s.add(i)

print(s)