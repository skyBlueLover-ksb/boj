import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return sorted(anagrams.values(), key=lambda x:len(x))
