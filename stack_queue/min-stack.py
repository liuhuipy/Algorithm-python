"""
最小栈：
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
示例:
    输入：
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
    输出：
        [null,null,null,null,-3,null,0,-2]
    解释：
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   --> 返回 -3.
        minStack.pop();
        minStack.top();      --> 返回 0.
        minStack.getMin();   --> 返回 -2.
方法：
    用额外一个栈记录每次push的数当前最小的值即可。
"""
import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.temp_stack = [math.inf]

    def push(self, x: int) -> None:
        self.temp_stack.append(self.temp_stack[-1] if self.temp_stack[-1] < x else x)
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.temp_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.temp_stack[-1]
