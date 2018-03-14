#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def SuiPianLength(self, strl):
        if len(strl) == 1:
            return 1
        pivot = strl[0]
        n = 1
        for i in range(1,len(strl)):
            if strl[i] == pivot:
                pass
            else:
                n+=1
                pivot = strl[i]
        resNum = '%.2f' % (len(strl) / n)
        return resNum

if __name__ == '__main__':
    strl = str(input())
    solut = Solution()
    resNum = solut.SuiPianLength(strl)
    print(resNum)
