# 🌳 102. Binary Tree Level Order Traversal

> **LeetCode #102 | Medium**

This repository contains my Python solution for **Binary Tree Level Order Traversal**, solved using **Breadth-First Search (BFS)** and a **Queue**.

---

## 📖 Problem Statement

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values.

The traversal should visit nodes **level by level**, moving from **left to right** within each level.

**LeetCode Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/

---

## 🧠 Solution Strategy

The problem is naturally suited for **Breadth-First Search (BFS)** because BFS explores nodes one level at a time.

### Approach

- Handle the empty tree case.
- Initialize a queue with the root node.
- While the queue is not empty:
  - Determine the number of nodes in the current level.
  - Process every node in that level.
  - Store node values in a temporary list.
  - Add left and right child nodes to the queue.
- Append each completed level to the final result.

This guarantees that every level is processed independently and in the correct order.

---

## 💡 Why BFS?

Depth-First Search (DFS) explores one branch completely before moving to the next, making it less suitable for level-wise traversal.

Breadth-First Search naturally processes all nodes at the same depth before moving deeper, making it the ideal solution for this problem.

---

## ⏱️ Complexity Analysis

| Metric | Complexity |
|--------|------------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(n)** |

Where **n** is the total number of nodes in the binary tree.

---

## 📝 Python Solution

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level)

        return result
```

---

## ✅ Example

### Input

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Output

```text
[
  [3],
  [9,20],
  [15,7]
]
```

---

## 🔑 Key Learnings

- Understanding when to choose **BFS over DFS**.
- Using **deque** for efficient queue operations.
- Processing one level at a time using `len(queue)`.
- Working with Binary Trees in Python.

---

## 🛠️ Concepts Used

- Binary Tree
- Breadth-First Search (BFS)
- Queue
- Tree Traversal
- Python Collections (`deque`)

---

## 📂 Folder Structure

```text
102. Binary Tree Level Order Traversal/
│
├── Binary_Tree_Level_Order_Traversal.py
└── README.md
```

---

## 👨‍💻 Author

**Naveen Kushwaha**

Passionate about solving Data Structures and Algorithms problems while continuously improving problem-solving skills through daily LeetCode practice.

---

⭐ If you found this solution helpful, feel free to explore the rest of the repository.