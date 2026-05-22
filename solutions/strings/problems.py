"""
Strings — Interview Problems
==============================
String manipulation, sliding window, and pattern matching problems.
"""
from typing import List
from collections import Counter, defaultdict


# ─────────────────────────────────────────────────────────────────────────────
# 1. Valid Anagram
# Check if two strings are anagrams of each other.
# Time: O(n)  Space: O(1) — fixed 26-char alphabet
# ─────────────────────────────────────────────────────────────────────────────
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Valid Palindrome
# A string is a palindrome if after removing non-alphanumeric chars and
# lowercasing, it reads the same forwards and backwards.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# ─────────────────────────────────────────────────────────────────────────────
# 3. Longest Substring Without Repeating Characters
# Time: O(n)  Space: O(min(m,n)) where m = charset size
# ─────────────────────────────────────────────────────────────────────────────
def length_of_longest_substring(s: str) -> int:
    char_index: dict = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# 4. Longest Repeating Character Replacement
# Given string s and k replacements, find the longest substring with all same chars.
# Sliding window: window is valid when (window_size - max_freq) <= k
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def character_replacement(s: str, k: int) -> int:
    count: dict = {}
    left = max_freq = result = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 5. Minimum Window Substring
# Find the smallest window in s that contains all chars in t.
# Time: O(n)  Space: O(t)
# ─────────────────────────────────────────────────────────────────────────────
def min_window(s: str, t: str) -> str:
    if not t:
        return ""
    need = Counter(t)
    have = {}
    formed = 0
    required = len(need)
    left = 0
    result = ""
    result_len = float("inf")

    for right, c in enumerate(s):
        have[c] = have.get(c, 0) + 1
        if c in need and have[c] == need[c]:
            formed += 1
        while formed == required:
            window_len = right - left + 1
            if window_len < result_len:
                result_len = window_len
                result = s[left:right + 1]
            lc = s[left]
            have[lc] -= 1
            if lc in need and have[lc] < need[lc]:
                formed -= 1
            left += 1
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 6. Group Anagrams
# Group strings that are anagrams of each other.
# Time: O(n * k log k)  k = max string length
# ─────────────────────────────────────────────────────────────────────────────
def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: dict = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


# ─────────────────────────────────────────────────────────────────────────────
# 7. Encode and Decode Strings
# Encode a list of strings to a single string, then decode it back.
# Protocol: length#string (e.g., "5#hello3#foo")
# ─────────────────────────────────────────────────────────────────────────────
def encode(strs: List[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(encoded: str) -> List[str]:
    result = []
    i = 0
    while i < len(encoded):
        j = encoded.index('#', i)
        length = int(encoded[i:j])
        result.append(encoded[j + 1:j + 1 + length])
        i = j + 1 + length
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 8. Find All Anagrams in a String
# Return all start indices of anagram substrings of p in s.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []
    p_count = Counter(p)
    window = Counter(s[:len(p)])
    result = []
    if window == p_count:
        result.append(0)
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left_char = s[i - len(p)]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        if window == p_count:
            result.append(i - len(p) + 1)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 9. Longest Palindromic Substring
# Expand around center approach.
# Time: O(n²)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def longest_palindrome_substr(s: str) -> str:
    result = ""
    result_len = 0

    def expand(l: int, r: int) -> None:
        nonlocal result, result_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > result_len:
                result = s[l:r + 1]
                result_len = r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)      # odd length
        expand(i, i + 1)  # even length
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 10. Roman to Integer
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def roman_to_int(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total
