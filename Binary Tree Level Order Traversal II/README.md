# Binary Tree Level Order Traversal II

## Description

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.

The traversal visits nodes level by level from left to right, starting from the leaf level and ending at the root.

## Approach

- Use **Breadth-First Search (BFS)** with a queue.
- Traverse the tree level by level.
- Store each level's values in the result.
- Reverse the result to obtain the bottom-up order.

## Concepts Used

- Binary Tree
- Breadth-First Search (BFS)
- Queue
- `deque`
- Level Order Traversal

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)