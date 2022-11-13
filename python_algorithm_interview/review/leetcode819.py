import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if x not in banned]
        counter = Counter(words)
        return counter.most_common(1)[0][0]
