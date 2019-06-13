# -*- coding:utf-8 -*-

"""
设计一个支持push，pop，top操作，并能在常数时间内检索到最小元素的栈
* push(x) 将元素x推入栈中
* pop() 删除栈顶的元素
* top() 获取栈顶元素
* getMin() 检索栈中的最小元素
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> None:
        if self.stack1:
            return self.stack1.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def getMin(self) -> int:
        if self.stack1:
            return min(self.stack1)


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-1)
    # min_stack.push(0)
    min_stack.top()
    # min_stack.push(-3)
    print(min_stack.getMin())
    # print(min_stack.pop())
    min_stack.push(1)
    print(min_stack.top())
    print(min_stack.getMin())