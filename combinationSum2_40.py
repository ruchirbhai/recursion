# https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

nums = [10,1,2,7,6,1,5]
target = 8

result = []

def combination_sum2_40(nums):
    #call the helper function
    nums.sort()
    combination_sum2_helper(nums,0,[])
    return result

def combination_sum2_helper(data, index, slate):
    # Backtrack case
    if sum(slate) == target:
        result.append(slate[:])
        return
    elif sum(slate) > target:
        return

    
    #base case
    if index == len(data):
         #no op
         return
    
    # recursion case
    # ensure no dupllicates
    dup_count = 0
    for i in range(index, len(nums)):
        if nums[index] != nums[i]:
            break
        dup_count += 1
    # exclude
    combination_sum2_helper(data, index+dup_count, slate)

    #include case
    for _ in range(0, dup_count):
        slate.append(data[index])
        combination_sum2_helper(data, index+dup_count, slate)
    
    for _ in range(0, dup_count):
        slate.pop()

    return


print(combination_sum2_40(nums))
