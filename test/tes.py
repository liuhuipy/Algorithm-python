#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def Find(self,target,array):
        row=0
        col=len(array)-1
        num = len(array[0])-1
        while(col>=0 and row<=num):
            m=array[col][row]
            if m == target:
                return True

            elif target>m:
                 row=row+1
            else:
                col=col-1
        return False

if __name__ == '__main__':
    array = [
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15],
    ]
    solut = Solution()
    res = solut.Find(5, array)
    print(res)