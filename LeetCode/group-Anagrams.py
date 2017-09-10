#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 2:
            return [strs]
        resStrs, dic = [], {}
        for str in strs:
            sortStr = ''.join(sorted(str))
            if sortStr in dic:
                dic[sortStr] += [str]
            else:
                dic[sortStr] = [str]
        for i in dic:
            tmp = dic[i]
            tmp.sort()
            resStrs += [tmp]
        return resStrs


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    #strs1 = ['']
    solut = Solution()
    resStrs = solut.groupAnagrams(strs)
    print(resStrs)