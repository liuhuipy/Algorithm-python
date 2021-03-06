"""
前k个高频元素：
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]
示例 2:
    输入: nums = [1], k = 1
    输出: [1]
提示：
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
    题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
    你可以按任意顺序返回答案。

方法：
    hashmap + 堆
"""
from typing import List
import heapq
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_map = collections.defaultdict()
        for num in nums:
            temp_map.setdefault(num, 0)
            temp_map[num] += 1

        max_heap = []
        for num, val in temp_map.items():
            if len(max_heap) < k:
                heapq.heappush(max_heap, (val, num))
            else:
                heapq.heappushpop(max_heap, (val, num))
        return [item[1] for item in max_heap]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4], 2))