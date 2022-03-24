from typing import List
import collections, heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        answer = list(list(zip(*counter.most_common(k)))[0])

        return answer

s = Solution()
print(s.topKFrequent([1,2],2))