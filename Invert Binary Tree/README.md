# 226. Invert Binary Tree

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/invert-binary-tree/

## Problem
Given the root of a binary tree, invert the tree, and return its root.

## Approach
DFS (recursive) — at each node, swap its left and right children, then
recursively apply the same operation to both subtrees.

## Example
\`\`\`
Input:  root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
\`\`\`

## Complexity
- **Time:** O(n) — every node visited once
- **Space:** O(h) — recursion stack depth (h = tree height)