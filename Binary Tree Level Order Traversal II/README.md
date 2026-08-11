# 🌳 Binary Tree Level Order Traversal II

> LeetCode Problem — Bottom-Up Level Order Traversal of a Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topic](https://img.shields.io/badge/Topic-Tree%20%7C%20BFS-blue)
![Language](https://img.shields.io/badge/Language-Python3-green?logo=python&logoColor=white)

---

## 📋 Problem Statement

Given the `root` of a binary tree, return **the bottom-up level order traversal** of its nodes' values — i.e., from left to right, level by level, **starting from the leaf level and ending at the root**.

---

## 📝 Example

**Input:**
```
root = [3,9,20,null,null,15,7]
```

```
        3
       / \
      9   20
         /  \
        15   7
```

**Output:**
```
[[15,7],[9,20],[3]]
```

Notice how the traversal starts from the **deepest level** (leaves) and works its way **up** to the root — the reverse of a normal top-down level order traversal.

---

## 💡 Approach

1. Perform a standard **BFS (Breadth-First Search)** using a queue (`deque`), processing the tree level by level as usual.
2. At each level, collect all node values into a list.
3. Append each level's list to the result.
4. Once the BFS is complete, **reverse the final result list** — this converts the normal top-down order into the required bottom-up order.

---

## 🧑‍💻 Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result[::-1]
```

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Explanation |
|---|---|---|
| **Time** | `O(n)` | Every node is visited and processed exactly once |
| **Space** | `O(n)` | The queue and result list can hold up to `n` nodes in the worst case (a wide tree) |

---

## 🔑 Key Takeaways

- This is a classic **BFS / Level Order Traversal** pattern — very common in tree-based interview questions
- The only difference from a normal level order traversal is the **final reversal** (`result[::-1]`) of the collected levels
- Using `deque` (instead of a regular list) makes `popleft()` an **O(1)** operation, keeping the whole algorithm efficient

---

## 🔗 Related Problems

- Binary Tree Level Order Traversal (Top-Down)
- Binary Tree Zigzag Level Order Traversal
- Average of Levels in Binary Tree
- Maximum Depth of Binary Tree