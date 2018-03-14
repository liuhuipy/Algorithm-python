#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def test(self, list1, list2):
        res = {}
        n = 1
        for i in range(len(list2)):
            for j in range(len(list2[0])):
                res[n] = {list1[j]:list2[i][j]}
                n += 1
        return res


if __name__ == '__main__':
    list1 = ['name1','name2','name3']
    list2 = [
        ['1', '2', '3'],
        ['4', '5', '6'],
    ]
    solut = Solution()
    resDict = solut.test(list1, list2)
    print(resDict)
