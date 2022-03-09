import collections as cl


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: cl.deque = cl.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
