import array
from typing import List

def maxArea(height: List[int]) -> int:
	width = list(enumerate([True] * len(height)))
	left = width[0][0]
	right = width[-1][0]
	heights = sorted(enumerate(height), key=lambda x: x[1])
	result = 0
	for i, h in heights[:-1]:
		area = h * max(i - left, right - i)
		if area > result:
			result = area
		width[i] = (i, False)
		if i == left:
			for j, active in width[left:right]:
				if active:
					left = j
					break
		elif i == right:
			for j, active in reversed(width[left:right]):
				if active:
					right = j
					break
	return result
print(maxArea([2,1]))