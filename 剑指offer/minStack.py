#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]


if __name__ == '__main__':
    solut = Solution()
    solut.push(5)
    solut.push(7)
    solut.push(4)
    print(solut.stack,solut.minStack)
    print(solut.min())
    solut.push(3)
    solut.push(2)
    print(solut.min())
    solut.pop()
    print(solut.min())
    print(solut.stack, solut.minStack)
    solut.pop()
    print(solut.min())
    print(solut.stack, solut.minStack)
