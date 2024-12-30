"""
Example 2: 2270. Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
"""

# problem done on leetcode - passed first try!!

def waysToSplitArray(self, nums):
        prefix = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        for split in range(len(nums)-1):
            first_sum = prefix[split]
            second_sum = prefix[-1] - prefix[split]
            if first_sum >= second_sum:
                ans += 1
        return ans
