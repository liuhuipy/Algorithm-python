#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class SeqList(object):

    def __init__(self, max=8):
        self.max = max              #创建默认为8
        self.num = 0
        self.date = [None] * self.max
