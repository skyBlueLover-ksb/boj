from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        volume = 0
        while left != right:
            if left_max <= right_max:
                volume += abs(left_max - height[left])
                left += 1
            else:
                volume += abs(right_max - height[right])
                right -= 1

            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        return volume
# s = Solution()
# height = [4,2,0,3,2,5]
# print(Solution.trap(s,height))