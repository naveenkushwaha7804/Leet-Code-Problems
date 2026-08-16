# Combinations

**LeetCode #77 — Medium**

## Problem

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

The order of elements does not matter, so `[1,2]` and `[2,1]` are considered the same combination.

## Approach

The solution uses **Backtracking** to generate all possible combinations.

- Start from `1` and explore numbers up to `n`.
- Add a number to the current combination.
- Recursively choose the next numbers.
- When the combination reaches size `k`, add a copy to the result.
- Backtrack by removing the last chosen element.

## Example

**Input:**
```text
n = 4, k = 2