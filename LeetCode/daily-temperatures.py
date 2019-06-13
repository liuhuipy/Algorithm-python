# -*- coding:utf-8 -*-

"""
根据每日气温列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。
如果之后都不会升高，请输入0来代替。
例如，给定一个列表temperatures=[73,74,75,71,69,72,76,73]，你的输出应该是[1,1,4,2,1,1,0,0]
"""


class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        index_stack = []
        for i in range(len(T)-1, -1, -1):
            while index_stack and T[i] >= T[index_stack[-1]]:
                index_stack.pop()
            res[i] = index_stack[-1] - i if index_stack else 0
            index_stack.append(i)
        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solut = Solution()
    print(solut.dailyTemperatures(temperatures))