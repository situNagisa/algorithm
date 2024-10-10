from typing import List


def moveZeroes(nums: List[int]) :
	result = [x for x in nums if x != 0]
	nums[:] = result + [0] * (len(nums) - len(result))
	return nums

print(moveZeroes([0,1,0,3,12]))