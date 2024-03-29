class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]

        if len(s) <= 1 or s == s[::-1]:
            return s

        result = ""

        for i in range(len(s)-1):
           result = max(
               expand(i, i+1),
               expand(i, i+2),
               result, key=lambda x: len(x))

        return result




