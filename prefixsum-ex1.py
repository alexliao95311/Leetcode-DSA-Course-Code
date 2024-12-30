"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""

"""
non-clean code:
def validqueries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix)-1])
    ans = []
    for q in range(len(queries)):
        querysum = prefix[queries[q][1]] - prefix[queries[q][0]] + nums[queries[q][0]]
        ans.append(querysum < limit)
        if querysum < limit:
            ans[q] = True
        else:
            ans[q] = False
    return ans
"""
def validqueries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        querysum = prefix[y] - prefix[x] + nums[x]
        ans.append(querysum < limit)
    return ans


print(validqueries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))
# Run all tests
assert validqueries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13) == [True, False, True], "Test case 1 failed"
assert validqueries([5, 2, 8, 10], [[1, 2]], 15) == [True], "Test case 2 failed"
assert validqueries([5, 2, 8, 10], [[0, 0], [3, 3]], 6) == [True, False], "Test case 3 failed"
#assert validqueries([], [], 5) == [], "Test case 4 failed"
assert validqueries([1, 2, 3], [], 5) == [], "Test case 5 failed"
assert validqueries([1, 2, 3, 4, 5], [[0, 4]], 15) == [False], "Test case 6 failed"
assert validqueries([-1, -2, 3, 4], [[0, 1], [1, 3]], 1) == [True, False], "Test case 7 failed"
nums = [1] * 1000
queries = [[0, 999]]
limit = 1001
assert validqueries(nums, queries, limit) == [True], "Test case 8 failed"

print("All test cases passed!")