#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        self.resList = []
        self.choiceSort(tinput, k)
        return self.resList

    def choiceSort(self, tinput, k):
        n = 1
        while n<=k:
            minN = tinput[0]
            for i in range(0,len(tinput)):
                if tinput[i] < minN:
                    minN = tinput[i]
            tinput.remove(minN)
            self.resList.append(minN)
            n += 1

if __name__ == '__main__':
    array = [4,5,1,6,2,7,3,8]
    solut = Solution()
    resList = solut.GetLeastNumbers_Solution(array, 10)
    print(resList)