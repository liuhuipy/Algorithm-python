#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys
def minnum(lst,initlist):
   lst=set(lst)
   initlist=set(initlist)
   lst.update(initlist)
   lst=list(lst)
   half=len(lst)//2
   return (lst[half]+lst[~half])/2
n=int(input())
lst=list(map(int,sys.stdin.readline().strip().split()))
num=int(input())
initlist=list(map(int,sys.stdin.readline().strip().split()))
print(minnum(lst,initlist))