#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



if __name__ == '__main__':
    solut = Solution()
    solut.push(10)
    solut.push(11)
    solut.push(12)
    print(solut.pop())
    solut.push(13)
    print(solut.pop())
    print(solut.pop())
    print(solut.pop())
    print(solut.pop())





