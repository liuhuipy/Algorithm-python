"""
分隔链表：
    给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
    每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
    这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
    返回一个符合上述规则的链表的列表。
    举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例：
    输入:
    root = [1, 2, 3], k = 5
    输出: [[1],[2],[3],[],[]]
    解释:
    输入输出各部分都应该是链表，而不是数组。
    例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
    第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
    最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。

"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        link_list_length = 0
        temp_node = root
        while temp_node:
            link_list_length += 1
            temp_node = temp_node.next

        enum = link_list_length % k
        min_child_array_length = link_list_length // k

        res = []
        temp = root
        for i in range(k):
            temp_child_arr_length = min_child_array_length + 1 if i < enum else min_child_array_length
            last_node = ListNode(-1)
            local_node = last_node
            for _ in range(temp_child_arr_length):
                if temp:
                    last_node.next = temp
                    last_node = temp
                    temp = temp.next
            res.append(local_node.next)
            last_node.next = None
        return res


# if __name__ == '__main__':
#     node1, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
#     node1.next, node2.next, node3.next = node2, node3, node4
#     solution = Solution()
#     solution.splitListToParts(node1, 5)
