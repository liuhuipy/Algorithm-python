#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

import sys

class Solution:
    def isPrimeNum(self, minN, maxN):
        suShuNum = 0
        for num in range(minN,maxN+1):
            if self.isPrime(num):
                suShuNum += 1
        return suShuNum

    def isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

if __name__ == '__main__':
    p = sys.stdin.readline().strip().split()
    minN = int(p[0])
    maxN = int(p[1])
    solut = Solution()
    res = solut.isPrimeNum(minN, maxN)
    print(res)
    #print(isPrime(13))
    #n = int(sys.stdin.readline().strip())

    '''
    num = 1
    count = 0
    while True:
        num += 1
        if isPrime(num):
            count += 1
        if count == n:
            break
    print(num)
    '''







