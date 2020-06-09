# https://leetcode.com/problems/subsets/
# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

nums = [1,2,3]
result = []

def subsets(nums):
    # pass the int array with index 0 and start with an empty array which will be out slate
    subset_helper(nums, 0, [])
    return result

def subset_helper(data, index, slate):
    #base case
    if index == len(data):
        # result.append(slate) 
        # If we used slate instead of slate[:] out output will be all empty strings
        # this is beacuse even though it will build the strings correctly the slate will pop the element out
        # Thus all the recursive function will be reference to the empty slate instead of a snapshot
        # slate[:] forces a snapshot copy instead of refrence to the variable slate
        result.append(slate[:])
        return

    # recursion case always 2 choices to either exclude or include
    # Exclude case no need to increase the slate just pass the slate with index incremeant
    subset_helper(data,index+1,slate)

    # Include case we need to change the slate to add the variable
    slate.append(data[index])
    subset_helper(data,index+1, slate)
    slate.pop()

    return


print(subsets(nums))