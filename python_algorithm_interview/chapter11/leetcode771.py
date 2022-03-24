import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        answer = 0
        for jewel in jewels:
            answer+=counter[jewel]
        return answer