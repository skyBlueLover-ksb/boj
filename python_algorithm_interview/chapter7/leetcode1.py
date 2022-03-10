from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             complement = target - n
#             if complement in nums[i+1:]:
#                 return [i, nums[i+1:].index(complement)+i+1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict([(j,i) for i, j in enumerate(nums)])

        for i, num in enumerate(nums):
            if target - num in nums_map and i!=nums_map[target-num]:
                return [i,nums_map[target-num]]



