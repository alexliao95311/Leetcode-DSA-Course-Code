"""
Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted
"""

def combinesortedarray(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

print(combinesortedarray([1, 3, 5, 7], [2, 4, 8, 9]))