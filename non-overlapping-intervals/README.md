# 435. Non-overlapping Intervals

**Difficulty:** Medium  
**Topics:** Greedy, Sorting  
**Link:** https://leetcode.com/problems/non-overlapping-intervals/

## Problem
Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

## Approach
- Sort intervals by start time
- Greedily merge/compare with the last kept interval
- If current interval overlaps with previous, keep the one with smaller end time (drop the "worse" one)
- Else, add current interval to result
- Answer = total intervals - length of non-overlapping result

## Complexity
- Time: O(n log n) — dominated by sorting
- Space: O(n) — for result array

## Code
See `solution.py`