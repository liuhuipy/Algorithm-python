"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例：
    输入：[1,2,3,4,5,6,7] 和 k = 3
    输出：[5,6,7,1,2,3,4]
说明：
    尽量想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求空间复杂度为O(1)的原地算法。
"""


class Solution:

    def rotate(self, nums: list, k: int) -> None:
        pass

    def rotate1(self, nums: list, k: int) -> None:
        """
        暴力求解：
            时间复杂度：O(n * k)
            空间复杂度：O(1)
        """
        if not nums:
            return
        len_nums = len(nums)
        for _ in range(k):
            last_num = nums[len_nums - 1]
            for i in range(len_nums - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last_num


# if __name__ == '__main__':
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     solution = Solution()
#     solution.rotate(nums, k)
#     print(nums)

