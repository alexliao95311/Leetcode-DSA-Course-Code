"""
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.
"""


# algo - iterate thru nums and look for its complement (target-nums)
#using an array to lookup complement = O(n), but for hashmap = O(1)
def twosum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in hashmap:
            return [i, hashmap[c]]
    hashmap[nums[i]] = i

#testing done on leetcode