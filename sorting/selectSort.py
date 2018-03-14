#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

def select_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist
    for i in range(length):
        index = i
        j = i + 1
        while j < length:
            if alist[j] < alist[index]:
                index = j
            j += 1
        temp = alist[index]
        alist[index] = alist[i]
        alist[i] = temp

if __name__ == '__main__':
    alist = [5,1,8,6,3,9,2,7,4]
    select_sort(alist)
    print(alist)