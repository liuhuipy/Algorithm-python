#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class Solution:
    def SimpleUnixLujin(self, s):
        if not s:
            return ''
        res = ''
        resStr = ''
        for i in range(len(s)):
            res += s[i]
            if res == '/../':
                index = resStr.rindex('/')
                resStr = resStr[:index]
                res = '/'
            elif res == '/./':
                res = '/'
            elif res[0] == '/' and len(res) > 2 and res[-1] == '/':
                n = len(res)
                resStr += res[:n-1]
                res = '/'
            elif res[-1] == '/' and res[0] != '/':
                resStr += res[:len(res)-1]
                res = '/'
            elif res[0] == '/' and len(res) > 1 and res[-1] == '/':
                if i + 1 >= len(s):
                    if s[i+1] != '/':
                        length = len(res)
                        if length % 2 != 0:
                            res = '/'
                            resStr += '/'
                        else:
                            res = '/'
                            resStr += '//'
                else:
                    length = len(res)
                    if length % 2 != 0:
                        res = '/'
                        resStr += '/'
                    else:
                        res = '/'
                        resStr += '//'
            else:
                pass
        return resStr

if __name__ == '__main__':
    s = input()
    solut = Solution()
    resStr = solut.SimpleUnixLujin(s)
    print(resStr)
