from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        local_num, i, index, len_num = nums[0], 1, 1, len(nums)
        while index < len_num:
            if nums[i] == local_num:
                del nums[i]
            else:
                local_num = nums[i]
                i += 1
            index += 1
        return len(nums)