"""
优美的排列II：
    给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：
    ① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中
    应该有且仅有 k 个不同整数；
    ② 如果存在多种答案，你只需实现并返回其中任意一种.
示例 1:
    输入: n = 3, k = 1
    输出: [1, 2, 3]
    解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
示例 2:
    输入: n = 3, k = 2
    输出: [1, 3, 2]
    解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
提示:
    n 和 k 满足条件 1 <= k < n <= 104.

方法1：
    全排列+计算每个排列元素间差的绝对值的个数。
    时间复杂度为O(n!)，空间复杂度为O(n)。
方法2：
    构造。需要敏捷的数学思维。
    当k=n-1时，有效的构造是[1,n,2,n-1,3,n-2,...]，这样构成的差绝对值[|n-1|,|n-2|,|n-3|,|n-4|,...,1]有n-1个。
    同理对于每个满足条件1<=k<n的k值，都可以构造出[1,k+1,2,k,3,k-1,4,k-2,...]这样已满足绝对值差不同的k+1个序列，剩余的n-k-1个数该
    如何处理呢。这样，我们把之前构造的序列每个数加上a（a=n-k-1），即[1+a,k+1+a,2+a,k+a,3+a,k-1+a,4+a,k-2+a,...]这样的序列依旧
    满足条件，然后把a的序列即[1,2,3,...,a]与之合并即可。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        a = n - k - 1
        left_arr = [i for i in range(1, a + 1)]
        right_arr = [k + 2 - i // 2 + a if i % 2 == 0 else (i + 1) // 2 + a for i in range(1, k + 2)]
        return left_arr + right_arr
