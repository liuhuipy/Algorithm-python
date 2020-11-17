"""
打家劫舍III：
    在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
    除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
     如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
    输入: [3,2,3,null,3,null,1]
         3
        / \
       2   3
        \   \
        3   1
    输出: 7
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
    输入: [3,4,5,1,3,null,1]
         3
        / \
       4   5
      / \   \
     1   3   1
    输出: 9
    解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if not node:
                return 0, 0
            un_choice_left, choice_left = dfs(node.left)
            un_choice_right, choice_right = dfs(node.right)
            return (
                    max(un_choice_left, choice_left) + max(un_choice_right, choice_right),
                    un_choice_left + un_choice_right + node.val
            )
        return max(dfs(root))


# if __name__ == '__main__': node1, node2, node3, node4, node5, node6 = TreeNode(3), TreeNode(4), TreeNode(5),
# TreeNode(1), TreeNode(3), TreeNode(1) node1.left, node1.right = node2, node3 node2.left, node2.right = node4,
# node5 node3.right = node6 print(Solution().rob(node1))
