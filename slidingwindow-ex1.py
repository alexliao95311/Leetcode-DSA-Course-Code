"""Let's say that we are given a positive integer array s and an integer k. We need to find the length of the longest subarray that has a sum less than or equal to k
"""

def findsubarray(s, k):
    max_len = 0
    sum = 0
    left = 0
    for right in range(len(s)):
        sum += s[right]
        while sum > k:
            sum -= s[left]
            left += 1
        max_len = max(max_len, right-left+1)
    if len(s) <= 1:
        if not s:
            return 0
        if s[0] == k:
            return 1
        else: 
            return 0
    return max_len


# Test cases
assert findsubarray([1, 2, 3, 4, 5], 9) == 3, "Test case 1 failed: Basic test case"
assert findsubarray([5], 5) == 1, "Test case 2 failed: Single element less than k"
assert findsubarray([10], 5) == 0, "Test case 3 failed: Single element greater than k"
assert findsubarray([6, 7, 8], 5) == 0, "Test case 4 failed: All elements greater than k"
assert findsubarray([0, 0, 0, 0], 5) == 4, "Test case 5 failed: Array with all zeros"
assert findsubarray([0, 1, 2, 0, 3], 3) == 4, "Test case 6 failed: Mixed zeros and positives"
assert findsubarray([1, 2, 3, 4, 5], 0) == 0, "Test case 7 failed: k = 0"
assert findsubarray([], 5) == 0, "Test case 8 failed: Empty array"
assert findsubarray([1, 1, 1, 1, 1], 5) == 5, "Test case 9 failed: Largest subarray"
assert findsubarray([1, 2, 3], 6) == 3, "Test case 10 failed: k equals sum of all elements"

print("All test cases passed!")