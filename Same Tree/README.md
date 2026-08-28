# 100. Same Tree

**Difficulty:** Easy

## Problem
Given the roots of two binary trees `p` and `q`, check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Approach
Simple DFS recursion:
1. If both nodes are `None` → they match → return `True`
2. If only one is `None` (other exists) → mismatch → return `False`
3. If values differ → return `False`
4. Recurse on left and right subtrees, both must match

## Complexity
- **Time:** O(n) — visits every node once
- **Space:** O(h) — recursion stack, h = height of tree

## Code
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)
```