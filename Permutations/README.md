# LeetCode 46 - Permutations

## Problem Statement

Given an array of **distinct integers**, return **all possible permutations** of the array.

A permutation is a unique arrangement of all the elements in the array.

**LeetCode Link:** https://leetcode.com/problems/permutations/

---

## Approach

This solution uses the **Backtracking** algorithm.

At each recursive call:

- Choose one element from the remaining numbers.
- Add it to the current permutation.
- Continue recursively with the remaining elements.
- Backtrack by removing the last selected element and exploring the next possibility.

Since every possible ordering is explored exactly once, all permutations are generated.

---

## Algorithm

1. Create an empty list to store the final result.
2. Define a recursive backtracking function.
3. If the current permutation contains all elements:
   - Store a copy in the result.
4. Otherwise:
   - Iterate through all remaining numbers.
   - Choose one number.
   - Recurse with the remaining numbers.
   - Backtrack.

---

## Complexity Analysis

**Time Complexity:** `O(n × n!)`

- There are `n!` possible permutations.
- Copying each permutation takes `O(n)` time.

**Space Complexity:** `O(n)`

- Recursive call stack depth is `n`.
- (Excluding the output list.)

---

## Python Solution

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(perm, options):
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for i in range(len(options)):
                perm.append(options[i])
                backtrack(perm, options[:i] + options[i+1:])
                perm.pop()

        backtrack([], nums)
        return result
```

---

## Example

**Input**

```text
nums = [1,2,3]
```

**Output**

```text
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
```

---

## Key Concepts

- Backtracking
- Recursion
- Depth First Search (DFS)
- Permutations

---

## Folder Structure

```
Permutations/
│── Permutations.py
└── README.md
```

---

## Author

**Naveen Kushwaha**

GitHub: https://github.com/naveenkushwaha7804