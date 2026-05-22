# Python Interview Prep

> 100 Python coding interview questions with optimal solutions, complexity analysis, and a CLI to run and test them. Covers arrays, strings, trees, graphs, dynamic programming, and more.

![Python](https://img.shields.io/badge/python-3.10+-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Problems](https://img.shields.io/badge/problems-100+-orange)

```
$ python cli.py run arrays two_sum

============================================================
Problem: two_sum
Category: arrays
============================================================
Given an array of integers and a target, return indices of the two numbers
that add up to target. Time: O(n)  Space: O(n)

Sample Input: ([2, 7, 11, 15], 9)
Output:       [0, 1]
Expected:     [0, 1]
Status:       ✅ PASS  (0.012ms)
```

## Problem Categories

| Category | Problems | Key Patterns |
|----------|----------|-------------|
| **Arrays** | 15 problems | Two pointers, sliding window, hash map |
| **Strings** | 10 problems | Sliding window, pattern matching |
| **Trees** | 10 problems | DFS, BFS, recursion |
| **Graphs** | 7 problems | BFS/DFS, Union-Find, Dijkstra |
| **Dynamic Programming** | 10 problems | Memoization, tabulation, space optimization |
| **Sorting & Searching** | 8 problems | Binary search variants, quickselect |

## Problems List

### 🔢 Arrays & Hashing
1. Two Sum — `O(n)` hash map
2. Best Time to Buy and Sell Stock — `O(n)` one pass
3. Contains Duplicate — set lookup
4. Product of Array Except Self — prefix/suffix without division
5. Maximum Subarray — Kadane's algorithm
6. Maximum Product Subarray — track min and max
7. Find Minimum in Rotated Sorted Array — binary search
8. Search in Rotated Sorted Array — modified binary search
9. 3Sum — sort + two pointers
10. Container With Most Water — two pointers
11. Merge Intervals — sort + greedy
12. Longest Consecutive Sequence — `O(n)` hash set
13. Trapping Rain Water — two pointers `O(n)`
14. Top K Frequent Elements — bucket sort
15. Sliding Window Maximum — monotonic deque

### 📝 Strings
1. Valid Anagram
2. Valid Palindrome
3. Longest Substring Without Repeating Characters
4. Longest Repeating Character Replacement
5. Minimum Window Substring
6. Group Anagrams
7. Encode and Decode Strings
8. Find All Anagrams in a String
9. Longest Palindromic Substring
10. Roman to Integer

### 🌲 Trees
1. Maximum Depth of Binary Tree
2. Invert Binary Tree
3. Diameter of Binary Tree
4. Balanced Binary Tree
5. Same Tree
6. Level Order Traversal
7. Lowest Common Ancestor of BST
8. Binary Tree Right Side View
9. Validate Binary Search Tree
10. Serialize and Deserialize Binary Tree

### 🕸️ Graphs
1. Number of Islands
2. Clone Graph
3. Course Schedule (cycle detection)
4. Walls and Gates (multi-source BFS)
5. Dijkstra's Shortest Path
6. Union-Find / Disjoint Set Union
7. Word Ladder

### 🧮 Dynamic Programming
1. Climbing Stairs (Fibonacci)
2. House Robber
3. House Robber II (circular)
4. Longest Increasing Subsequence — `O(n log n)`
5. Coin Change
6. 0/1 Knapsack
7. Longest Common Subsequence
8. Edit Distance (Levenshtein)
9. Word Break
10. Unique Paths

---

## Setup

```bash
git clone https://github.com/bhupendra05/python-interview-prep.git
cd python-interview-prep
python cli.py list
```

No dependencies required — pure Python standard library.

## CLI Usage

```bash
# List all available problems
python cli.py list

# Run a specific problem with sample input
python cli.py run arrays two_sum
python cli.py run dynamic_programming coin_change
python cli.py run trees max_depth

# Run all tests for a category
python cli.py test arrays
python cli.py test dynamic_programming

# Run all tests
python cli.py test all
```

## Study Guide

### Interview Patterns (Master These)

**Two Pointers** — `two_sum`, `3sum`, `container_with_most_water`, `trapping_rain_water`
> Use when array is sorted or you need pairs/triplets. One pointer at each end moving inward.

**Sliding Window** — `longest_substring`, `minimum_window_substring`, `character_replacement`
> Use for contiguous subarray/substring problems. Expand right, shrink left.

**Fast & Slow Pointers** — cycle detection, finding middle of linked list
> Two pointers moving at different speeds.

**BFS** — `level_order`, `walls_and_gates`, `word_ladder`
> Shortest path in unweighted graphs. Use deque. Process level by level.

**DFS + Backtracking** — tree traversals, `num_islands`, `word_search`
> Explore all paths. Mark visited → recurse → unmark (backtrack).

**Dynamic Programming** — recognize overlapping subproblems
> 1D DP: Fibonacci, Climbing Stairs, House Robber
> 2D DP: LCS, Edit Distance, Unique Paths

**Binary Search** — `find_min`, `search_rotated`, `length_of_lis`
> Any time array is sorted OR answer space is monotonic.

### Complexity Reference

| Pattern | Time | Space |
|---------|------|-------|
| Two pointers | O(n) | O(1) |
| Sliding window | O(n) | O(k) |
| Hash map lookup | O(1) avg | O(n) |
| Binary search | O(log n) | O(1) |
| BFS/DFS | O(V+E) | O(V) |
| Sorting | O(n log n) | O(1)–O(n) |

## Project Structure

```
python-interview-prep/
├── cli.py                         # Run and test problems from terminal
└── solutions/
    ├── arrays/problems.py         # 15 array problems
    ├── strings/problems.py        # 10 string problems
    ├── trees/problems.py          # 10 tree problems
    ├── graphs/problems.py         # 7 graph problems
    └── dynamic_programming/
        └── problems.py            # 10 DP problems
```

## License

MIT © bhupendra05
