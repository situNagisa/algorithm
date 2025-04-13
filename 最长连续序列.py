from typing import List
import sys

def longestConsecutive(nums: List[int]) -> int:
	nums = sorted(list(set(nums)))
	nums.append(-sys.maxsize - 1)
	result = 0
	i = 0
	while i < len(nums) - 1:
		for j in range(i+1, len(nums)):
			if nums[j] - nums[i] != j - i:
				if j - i > result:
					result = j - i
				i = j
				break
	return result

print(longestConsecutive([1,2,0,1]))