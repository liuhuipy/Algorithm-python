
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder:
            return
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_index, root = 0, TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_index = i
                break
        if root_index:
            root.left = self.buildTree(preorder[1: root_index + 1], inorder[:root_index + 1])
        if root_index < len(inorder) - 1:
            root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root


# if __name__ == '__main__':
#     preorder = [3, 9, 20, 15, 7]
#     inorder = [9, 3, 15, 20, 7]
#     solution = Solution()
#     solution.buildTree(preorder, inorder)
