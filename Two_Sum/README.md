# LeetCode 1 - Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

### Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
```

### Example 2
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## Approach

Instead of checking every pair of numbers (which takes O(n²) time), we use a **hash map** to store numbers we've already seen along with their index.

For every number `num` at index `i`:
1. Calculate its `complement = target - num`.
2. Check if that `complement` already exists in the hash map.
   - If yes → we've found our pair, return `[seen[complement], i]`.
   - If no → store the current number and its index in the map, and move on.

This way, the array is traversed only **once**.

---

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
|--------|------------|--------------|
| Time   | `O(n)`     | Single pass through the array |
| Space  | `O(n)`     | Hash map storing up to `n` elements |

---

## Why Hash Map Over Brute Force?

| Approach      | Time Complexity | Space Complexity |
|---------------|------------------|-------------------|
| Brute Force (nested loop) | O(n²) | O(1) |
| Hash Map (this solution)  | O(n)  | O(n) |

The hash map approach trades a bit of extra space for a significant improvement in time complexity, making it the optimal solution for this problem.

---

## Tags
`Array` `Hash Table` `LeetCode` `Python`