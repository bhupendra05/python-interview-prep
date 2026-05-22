"""
Dynamic Programming — Interview Problems
==========================================
Classic DP problems from easy to hard.
Pattern: Identify state → recurrence → base case → optimize space.
"""
from typing import List


# ─────────────────────────────────────────────────────────────────────────────
# 1. Climbing Stairs
# Count ways to reach top climbing 1 or 2 steps.
# Pattern: Fibonacci  Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ─────────────────────────────────────────────────────────────────────────────
# 2. House Robber
# Max money robbing adjacent houses without hitting two in a row.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def rob(nums: List[int]) -> int:
    prev2 = prev1 = 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1


# ─────────────────────────────────────────────────────────────────────────────
# 3. House Robber II (circular street)
# Rob max from circular array — run rob() twice: [0..n-2] and [1..n-1].
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def rob_circular(nums: List[int]) -> int:
    def rob_linear(houses):
        prev2 = prev1 = 0
        for h in houses:
            prev2, prev1 = prev1, max(prev1, prev2 + h)
        return prev1

    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ─────────────────────────────────────────────────────────────────────────────
# 4. Longest Increasing Subsequence
# Time: O(n log n) with patience sorting  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
import bisect

def length_of_lis(nums: List[int]) -> int:
    tails = []  # tails[i] = smallest tail of LIS of length i+1
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails):
            tails.append(n)
        else:
            tails[pos] = n
    return len(tails)


# ─────────────────────────────────────────────────────────────────────────────
# 5. Coin Change
# Min coins to make amount. Classic unbounded knapsack.
# Time: O(amount * len(coins))  Space: O(amount)
# ─────────────────────────────────────────────────────────────────────────────
def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# ─────────────────────────────────────────────────────────────────────────────
# 6. 0/1 Knapsack
# Max value fitting items in capacity (each item used at most once).
# Time: O(n * W)  Space: O(W)
# ─────────────────────────────────────────────────────────────────────────────
def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):  # reverse to avoid using same item twice
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


# ─────────────────────────────────────────────────────────────────────────────
# 7. Longest Common Subsequence
# Time: O(m*n)  Space: O(min(m,n))
# ─────────────────────────────────────────────────────────────────────────────
def lcs(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    prev = [0] * (len(text2) + 1)
    for c1 in text1:
        curr = [0] * (len(text2) + 1)
        for j, c2 in enumerate(text2):
            curr[j + 1] = prev[j] + 1 if c1 == c2 else max(prev[j + 1], curr[j])
        prev = curr
    return prev[len(text2)]


# ─────────────────────────────────────────────────────────────────────────────
# 8. Edit Distance (Levenshtein)
# Min operations (insert, delete, replace) to convert word1 to word2.
# Time: O(m*n)  Space: O(min(m,n))
# ─────────────────────────────────────────────────────────────────────────────
def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp
    return dp[n]


# ─────────────────────────────────────────────────────────────────────────────
# 9. Word Break
# Can string s be segmented into words from wordDict?
# Time: O(n²)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]


# ─────────────────────────────────────────────────────────────────────────────
# 10. Unique Paths
# Count paths from top-left to bottom-right (only right or down moves).
# Time: O(m*n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]
