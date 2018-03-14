#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import sys

class Solution:

    def JiEZhi(self, n, m, arr, tes):
        a = sorted(tes.keys())
        resJiE = []
        for i in range(n-1,-1,-1):
            jieZhi = tes.get(a[i])
            print(jieZhi)
            jieZhi = self.jiE(arr, jieZhi)
            resJiE.append(jieZhi)

    def jiE(self, arr, jieZhi):
        k = m
        while arr[0] <= jieZhi:
            for i in range(k):
                if arr[0] > jieZhi:
                    return jieZhi
                if arr[i] > jieZhi:
                    chi = arr[i - 1]
                    arr.remove(arr[i - 1])
                    k = i - 1
                    print(arr)
                    break
                if i == m - 1:
                    chi = arr[i]
                    arr.remove(arr[i])
                    k = i - 1
                    print(arr)
            jieZhi -= chi
        return jieZhi


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip().split()
    n = int(line1[0])
    m = int(line1[1])
    line2 = sys.stdin.readline().strip().split()
    arr = []
    for i in range(m):
        arr.append(int(line2[i]))
    tes = {}
    for i in range(2):
        linei = sys.stdin.readline().strip().split()
        tes.setdefault(int(linei[0]),int(linei[1]))
    print(tes)
    solut = Solution()
    res = solut.JiEZhi(n, m, arr, tes)
    print(res)
