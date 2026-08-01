# 217. Contains Duplicate

## 📝 Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.

**LeetCode Link:** https://leetcode.com/problems/contains-duplicate/

---

## 💡 Approach

The solution uses Python's built-in `set`.

- A `set` stores only unique elements.
- If the length of the original array is different from the length of the set, it means duplicate values exist.
- Otherwise, all elements are unique.

This approach is simple, efficient, and takes advantage of Python's built-in data structures.

---

## ✅ Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

---

## ⏱️ Complexity Analysis

| Operation | Complexity |
|-----------|------------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## 📚 Key Concepts

- Hash Set (`set`)
- Array
- Duplicate Detection
- Python Built-in Data Structures

---

## 🚀 Learning Outcome

This problem demonstrates how a hash set can quickly identify duplicate elements without using nested loops, reducing the time complexity from **O(n²)** to **O(n)**.

---

⭐ If you found this solution helpful, feel free to explore the rest of my LeetCode solutions in this repository.