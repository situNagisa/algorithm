from typing import List
from itertools import accumulate
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums))
        c = Counter(prefix_sum)
        prefix_sum = [0] + prefix_sum
        result = 0
        for n, nn in zip(prefix_sum[:-1], prefix_sum[1:]):
            result += c[n + k]
            c[nn] -= 1
        return result
# 1, 2, 3
#   1, 3, 6
#   2, 5
#   3
# 1, 3, 6
#   2, 5
#   3,
#
# 0, 1, 3, [6]
#   1, 3, 6
#   2, 5,
#   3
# 3, 4, 6

# 1
#   1
# 1
#
# 0, [1]
#   1

# -1, -1, 1
#   -1, -2, -1
#   -1, 0
#   1,
# -1, -2, -1
#   -1, 0
#   1
# 0, -1, -2, [-1]
#   -1, -2, -1
#   -1, 0,
#   1,
# 0, -1, -2

# 1, -1, 0
# 1, 0, 0
# 0, 1, 0, [0]
#   1, 0, 0
#   -1, -1
#   0


print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([1,], 0))
print(Solution().subarraySum([-1,-1,1], 0))
print(Solution().subarraySum([1,-1,0], 0))