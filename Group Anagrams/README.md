# 49. Group Anagrams

## Problem

Given an array of strings `strs`, group all the strings that are anagrams of each other. The output can be returned in any order.

**LeetCode:** https://leetcode.com/problems/group-anagrams/

**Difficulty:** Medium

---

## My Approach

The main idea is to use a hash map to group words that have the same characters.

For each word, I sort its characters and use the sorted string as a key in the dictionary. Since anagrams contain the same letters, their sorted form will always be identical. I then store the original word in the list corresponding to that key.

After processing all the words, the values of the dictionary contain the required groups of anagrams.

---

## Complexity Analysis

- **Time Complexity:** `O(n × k log k)`
- **Space Complexity:** `O(n × k)`

Where:
- `n` is the number of strings.
- `k` is the average length of each string.

---

## Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            anagram[sorted_word].append(s)

        return list(anagram.values())
```

---

## Key Takeaways

- A sorted string can be used as a unique identifier for an anagram group.
- `defaultdict(list)` makes grouping elements simple and clean.
- This approach is efficient and easy to understand.

---

**Language:** Python

**Topic:** Hash Table, String, Sorting