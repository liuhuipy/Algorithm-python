"""
复原IP地址：
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
    例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
    和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：
    输入：s = "25525511135"
    输出：["255.255.11.135","255.255.111.35"]
示例 2：
    输入：s = "0000"
    输出：["0.0.0.0"]
示例 3：
    输入：s = "1111"
    输出：["1.1.1.1"]
示例 4：
    输入：s = "010010"
    输出：["0.10.0.10","0.100.1.0"]
示例 5：
    输入：s = "101023"
    输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

方法：
    DFS（回溯）
"""
from typing import List


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.helper(s, 4, [])
        return self.res

    def helper(self, s: str, need_distribute: int, temp_arr: List[str]):
        if need_distribute == 1 and self.check_ip(s):
            self.res.append(".".join([*temp_arr, s]))
            return
        if need_distribute == 0 or (need_distribute == 1 and not self.check_ip(s)):
            return
        if len(s) > 3 and self.check_ip(s[:3]):
            self.helper(s[3:], need_distribute - 1, [*temp_arr, s[:3]])
        if len(s) > 2 and self.check_ip(s[:2]):
            self.helper(s[2:], need_distribute - 1, [*temp_arr, s[:2]])
        if len(s) > 1 and self.check_ip(s[0]):
            self.helper(s[1:], need_distribute - 1, [*temp_arr, s[:1]])

    @staticmethod
    def check_ip(s):
        if len(s) == 1:
            return True
        if len(s) > 3 or s[0] == "0" or int(s) > 255:
            return False
        return True
