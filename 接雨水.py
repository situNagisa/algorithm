from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        falls: list[tuple[int, int]] = []
        capacity: int = 0
        for i_index, i in enumerate([height[ii + 1] - height[ii] for ii in range(len(height[:-1]))]):
            if i < 0:
                falls.append((i, 1))
                continue
            if not len(falls):
                continue
            if i == 0:
                falls[-1] = falls[-1][0], falls[-1][1] + 1
                continue
            if i > 0:
                d = i
                while True:
                    fall, step = falls[-1]
                    d += fall
                    if d < 0:
                        capacity += step * (d - fall)
                        falls[-1] = d, step + 1
                        break
                    if d == 0:
                        capacity += step * (-fall)
                        falls.pop()
                        if len(falls):
                            falls[-1] = falls[-1][0], falls[-1][1] + step + 1
                        break
                    if d > 0:
                        capacity += step * -fall
                        falls.pop()
                        if not len(falls):
                            break
                        falls[-1] = falls[-1][0], falls[-1][1] +  step
                continue
        return capacity
                        
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))

            