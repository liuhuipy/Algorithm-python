#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'



if __name__ == '__main__':
    s = [
        {'PC交易前台': 1022.0},
        {'手机接口':1022.0},
        {'PC交易前台': 1022.0},
        {'手机接口': 1022.0},
        {'PC交易前台': 1022.0},
        {'手机接口': 1022.0},
        {'PC交易前台': 1022.0},
        {'手机接口': 1022.0},
        {'PC交易前台': 6132.0},
        {'手机接口': 64343.0},
    ]
    res = {}
    for i, tes in enumerate(s):
        for m, item in tes.items():
            if m not in res:
                res[m] = [item]
            else:
                res[m] += [item]
    print(res)

