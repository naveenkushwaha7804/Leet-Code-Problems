from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            sorted_word = "".join(sorted(s))
            anagram[sorted_word].append(s)
        return list(anagram.values())
        