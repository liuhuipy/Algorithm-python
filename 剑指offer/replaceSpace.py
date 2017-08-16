#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:

    def replaceSpace(self, s):
        return s.replace(' ', '%20')


if __name__ == "__main__":
    str1 = 'We Are Happy'
    solut = Solution()
    result = solut.replaceSpace(str1)
    print(result)

