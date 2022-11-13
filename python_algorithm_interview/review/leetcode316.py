from collections import deque, Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        q = deque()
        seen = set()
        counter = Counter(s)

        for c in s:
            counter[c] -= 1
            if c in seen:
                continue

            while q and c < q[-1] and counter[q[-1]] > 0:
                seen.remove(q.pop())

            q.append(c)
            seen.add(c)

        return ''.join(q)
