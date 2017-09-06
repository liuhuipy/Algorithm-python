#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字
均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1
,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 1:
            if pushV != popV:
                return False
            return True
        if len(pushV) == 0:
            return True
        indexI = pushV.index(popV[0])
        self.stack = pushV[0:indexI]
        for i in range(1, len(popV)):
            if popV[i] in self.stack:
                if self.stack[-1] == popV[i]:
                    self.stack.pop()
                else:
                    return False
            elif popV[i] in pushV:
                pass
            else:
                return False
        return True



if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popV1 = [4, 3, 5, 1, 2]
    solut = Solution()
    res = solut.IsPopOrder(pushV, popV)
    print(res)