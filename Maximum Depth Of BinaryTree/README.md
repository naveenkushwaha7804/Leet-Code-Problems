# 104. Maximum Depth of Binary Tree

## Problem
Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node to the farthest leaf node.

## Approach
- Use **Depth First Search (DFS)**.
- Recursively calculate the depth of the left and right subtrees.
- Return the maximum of both subtree depths plus `1`.
- Return `0` when the current node is `None`.

## Example

Input:
```text
root = [3,9,20,null,null,15,7]