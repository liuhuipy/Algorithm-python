# -*- coding:utf-8 -*-


class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack, temp_dict = [], {'(': ')', '{': '}', '[': ']'}
        for sstr in s:
            if temp_stack and temp_stack[-1] in temp_dict and temp_dict[temp_stack[-1]] == sstr:
                temp_stack.pop()
            else:
                temp_stack.append(sstr)
        return not temp_stack


if __name__ == '__main__':
    s = "([)]"
    s2 = "()[]{}"
    solut = Solution()
    print(solut.isValid(s2))