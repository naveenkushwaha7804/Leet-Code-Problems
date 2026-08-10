# LeetCode 2812 - Find the Safest Path in a Grid

## Problem

You are given an `n × n` grid where:

- `1` represents a cell containing a thief.
- `0` represents an empty cell.

You start from the top-left cell `(0, 0)` and need to reach the bottom-right cell `(n-1, n-1)`.

The **safeness factor** of a path is defined as the minimum Manhattan distance from any cell in that path to the nearest thief.

The goal is to find the **maximum possible safeness factor** among all valid paths.

---

## Approach

This solution uses **Multi-Source BFS** and **Priority Queue (Max Heap)**.

### Step 1: Calculate Distance from the Nearest Thief

First, perform a Multi-Source BFS starting from all cells containing thieves.

For every cell, calculate its minimum Manhattan distance from the nearest thief.

This gives us a `dist` matrix where:

```text
dist[r][c] = minimum distance from (r, c) to any thief