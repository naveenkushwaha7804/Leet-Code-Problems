# 🏝️ Number of Islands

> LeetCode 200 — Count the number of islands in a 2D binary grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topic](https://img.shields.io/badge/Topic-DFS%20%7C%20BFS%20%7C%20Matrix-blue)
![Language](https://img.shields.io/badge/Language-Python3-green?logo=python&logoColor=white)

---

## 📋 Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return **the number of islands**.

An **island** is surrounded by water and is formed by connecting adjacent lands **horizontally or vertically**. You may assume all four edges of the grid are all surrounded by water.

---

## 📝 Example

**Input:**
```
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```

**Output:**
```
1
```

*(All the connected 1's form a single big island, so the answer is 1)*

---

## 💡 Approach

This is a classic **connected components** problem on a grid — solved using **DFS (Depth-First Search)**:

1. Loop through every cell in the grid
2. Whenever a `'1'` (land) is found that hasn't been visited yet, it means we've discovered a **new island** → increment the island count
3. From that cell, run a **DFS** that "sinks" the entire island — mark every connected `'1'` (up, down, left, right) as visited by turning it into `'0'`
4. This ensures the same island is never counted twice
5. Continue scanning the rest of the grid for more unvisited `'1'`s

---

## 🧑‍💻 Solution

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base case: out of bounds or water/visited cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            grid[r][c] = '0'  # mark as visited (sink the land)

            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
```

---

## ⏱️ Complexity Analysis

| Metric | Complexity | Explanation |
|---|---|---|
| **Time** | `O(m * n)` | Every cell is visited at most once |
| **Space** | `O(m * n)` | Worst case recursion stack depth if the entire grid is one big island |

---

## 🔑 Key Takeaways

- Classic **Flood Fill / Connected Components** pattern — same idea used in "Flood Fill", "Max Area of Island", "Surrounded Regions"
- DFS "sinks" visited land so we never revisit or double-count the same island
- Could also be solved using **BFS** (with a queue) or **Union-Find (Disjoint Set)** for large grids where recursion depth might cause a stack overflow

---

## 🔗 Related Problems

- Max Area of Island
- Flood Fill
- Surrounded Regions
- Number of Islands II
- Island Perimeter