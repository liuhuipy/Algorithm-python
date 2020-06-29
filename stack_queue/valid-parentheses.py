"""
有效的括号：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
        1.左括号必须用相同类型的右括号闭合。
        2.左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
    输入: "()"
    输出: true
方法：
    使用栈实现。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack = []
        temp_dic = {")": "(", "}": "{", "]": "["}
        for a in s:
            if a in ["(", "{", "["]:
                temp_stack.append(a)
            elif not temp_stack or temp_stack[-1] != temp_dic[a]:
                return False
            else:
                temp_stack.pop()
        return not temp_stack
