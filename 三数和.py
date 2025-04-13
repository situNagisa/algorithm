from typing import List, Optional
import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_table: dict[int, int] = {}
        for num in sorted(nums):
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1
        result: List[List[int]] = []
        list_key = list(hash_table.keys())
        for i_index, i in enumerate(list_key):
            if i > 0:
                break
            hash_table[i] -= 1
            j_begin = i_index if hash_table[i] > 0 else i_index + 1
            for j_index, j in enumerate(list_key[j_begin:]):
                if i + 2 * j > 0: # expect < j
                    break
                expect = -i - j
                hash_table[j] -= 1
                if expect in hash_table and hash_table[expect] > 0:
                    e = [i, min(j, expect), max(j, expect)]
                    # if e not in result:
                    #     result.append(e)
                    result.append(e)
                hash_table[j] += 1
            hash_table[i] += 1
        return result
            

s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))