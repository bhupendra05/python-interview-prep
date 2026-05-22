"""
Arrays & Hashing — Interview Problems
======================================
Classic array problems with optimal Python solutions.
Each function includes time/space complexity analysis.
"""
from typing import List, Optional
from collections import defaultdict, Counter


# ─────────────────────────────────────────────────────────────────────────────
# 1. Two Sum
# Given an array of integers and a target, return indices of the two numbers
# that add up to target. Each input has exactly one solution.
# Time: O(n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value → index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


# ─────────────────────────────────────────────────────────────────────────────
# 2. Best Time to Buy and Sell Stock
# Find the max profit from one buy + one sell (buy before sell).
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val


# ─────────────────────────────────────────────────────────────────────────────
# 3. Contains Duplicate
# Return True if any value appears at least twice.
# Time: O(n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


# ─────────────────────────────────────────────────────────────────────────────
# 4. Product of Array Except Self
# Return array where each element is product of all other elements.
# Must run in O(n) without using division.
# Time: O(n)  Space: O(1) (output array doesn't count)
# ─────────────────────────────────────────────────────────────────────────────
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements to the left
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right pass: multiply by product of all elements to the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# ─────────────────────────────────────────────────────────────────────────────
# 5. Maximum Subarray (Kadane's Algorithm)
# Find the contiguous subarray with the largest sum.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def max_subarray(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# ─────────────────────────────────────────────────────────────────────────────
# 6. Maximum Product Subarray
# Find the contiguous subarray with the largest product.
# Key insight: track both max and min (negative × negative = positive).
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def max_product(nums: List[int]) -> int:
    result = max(nums)
    cur_min = cur_max = 1
    for n in nums:
        if n == 0:
            cur_min = cur_max = 1
            continue
        candidates = (n * cur_max, n * cur_min, n)
        cur_max = max(candidates)
        cur_min = min(candidates)
        result = max(result, cur_max)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 7. Find Minimum in Rotated Sorted Array
# Array was rotated at some pivot. Find the minimum element.
# Time: O(log n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# ─────────────────────────────────────────────────────────────────────────────
# 8. Search in Rotated Sorted Array
# Binary search in a rotated array.
# Time: O(log n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def search_rotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ─────────────────────────────────────────────────────────────────────────────
# 9. 3Sum
# Find all unique triplets that sum to zero.
# Time: O(n²)  Space: O(n) for sorting
# ─────────────────────────────────────────────────────────────────────────────
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue  # skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = n + nums[left] + nums[right]
            if total == 0:
                result.append([n, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 10. Container With Most Water
# Given heights, find two lines forming the container with most water.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


# ─────────────────────────────────────────────────────────────────────────────
# 11. Merge Intervals
# Given a list of intervals, merge all overlapping ones.
# Time: O(n log n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ─────────────────────────────────────────────────────────────────────────────
# 12. Longest Consecutive Sequence
# Find length of the longest consecutive elements sequence. O(n) required.
# Time: O(n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:  # start of a sequence
            current = n
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest


# ─────────────────────────────────────────────────────────────────────────────
# 13. Trapping Rain Water
# Calculate how much water can be trapped after raining.
# Time: O(n)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def trap(height: List[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water


# ─────────────────────────────────────────────────────────────────────────────
# 14. Top K Frequent Elements
# Return the k most frequent elements.
# Time: O(n)  Space: O(n)  — uses bucket sort
# ─────────────────────────────────────────────────────────────────────────────
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 15. Sliding Window Maximum
# Return the max value in each sliding window of size k.
# Time: O(n)  Space: O(k)
# ─────────────────────────────────────────────────────────────────────────────
from collections import deque

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    result = []
    dq: deque = deque()  # stores indices, decreasing order of values

    for i, n in enumerate(nums):
        # Remove indices outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
