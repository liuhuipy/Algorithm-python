#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:

    def huiWen(self, number):

        numberstr = str(number)
        length1 = len(numberstr)
        length2 = int(length1 / 2)
        print(length2)
        j = length1 - 1
        for i in range(length2):
            if numberstr[i] != numberstr[j]:
                print(numberstr[i] + ':' + numberstr[j])
                return False
            else:
                print(numberstr[i] + ':' + numberstr[j])
            j -= 1
        else:
            return True


if __name__ == "__main__":
    number = 12345321
    solut = Solution()
    res = solut.huiWen(number)
    print(res)