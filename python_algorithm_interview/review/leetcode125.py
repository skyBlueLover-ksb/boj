from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque()

        for char in s:
            if char.isalnum():
                q.append(char.lower())

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
