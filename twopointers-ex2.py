"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given s = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

def twosumsorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:  # current_sum > target
            right -= 1
    return False

# Test cases for twosumsorted
assert twosumsorted([1, 2, 3, 4, 5], 9) == True, "Test case 1 failed"  # Pair exists (4+5)
assert twosumsorted([1, 2, 3, 4, 5], 10) == False, "Test case 2 failed"  # No such pair
assert twosumsorted([1, 3, 5, 7, 9], 12) == True, "Test case 3 failed"  # Pair exists (3+9)
assert twosumsorted([], 5) == False, "Test case 4 failed"  # Empty array
assert twosumsorted([5], 5) == False, "Test case 5 failed"  # Single element
assert twosumsorted([5, 5], 10) == True, "Test case 6 failed"  # Pair exists (both 5)
assert twosumsorted([1, 2, 3], 4) == True, "Test case 7 failed"  # Pair exists (1+3)
assert twosumsorted([1, 2, 3], 7) == False, "Test case 8 failed"  # No such pair
assert twosumsorted([-3, 0, 3, 4, 5], 0) == True, "Test case 9 failed"  # Pair exists (-3+3)
assert twosumsorted([1, 2, 2, 3, 4], 4) == True, "Test case 10 failed"  # Pair exists (2+2)
assert twosumsorted([1, 2, 3, 4, 6], 7) == True, "Test case 11 failed"  # Pair exists (3+4)

print("All test cases passed!")