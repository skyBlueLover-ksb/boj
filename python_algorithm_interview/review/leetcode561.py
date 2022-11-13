from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        nums.sort(reverse=True)
        for i in range(len(nums)//2):
            s+=nums[2*i+1]
        return s
