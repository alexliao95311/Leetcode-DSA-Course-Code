"""
Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111."""

def binarystring(s):
    left = 0
    ans = 0
    count_0 = 0
    for right in range(len(s)):
        if s[right] == "0":
            count_0 += 1
        while count_0 > 1:
            if s[left] == "0":
                count_0 -= 1
            left += 1
        ans = max(ans, right-left+1)
    return ans

# Test cases for binarystring
assert binarystring("1101100111") == 5, "Test case 1 failed: Flip at index 2 gives length 5"
assert binarystring("11111") == 5, "Test case 2 failed: Already all '1's"
assert binarystring("00000") == 1, "Test case 3 failed: Flip one '0' gives single '1'"
assert binarystring("101010") == 3, "Test case 4 failed: Max substring after one flip is 2"
assert binarystring("10001") == 2, "Test case 5 failed: Flip at index 1 or 3 gives length 3"
assert binarystring("1") == 1, "Test case 6 failed: Single '1'"
assert binarystring("0") == 1, "Test case 7 failed: Single '0', flip gives one '1'"
assert binarystring("10") == 2, "Test case 8 failed: Flip gives '11' with length 2"
assert binarystring("01") == 2, "Test case 9 failed: Flip gives '11' with length 2"
assert binarystring("") == 0, "Test case 10 failed: Empty string gives length 0"

print("All test cases passed!")