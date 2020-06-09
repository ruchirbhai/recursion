# https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

nums = [1,2,3]
result = []

def permutation_46(nums):
    perm_helper(nums, 0, [])
    return result


def perm_helper(data, index, slate):
    #base case
    if index == len(data):
        result.append(slate[:])
        return

    #recursion case for permutation internal node
    for pick in range(index,len(data)):
        # Here we need to swap pick with index value
        data[pick], data[index] = data[index], data[pick]
        # After the swap call the problem recutsively
        slate.append(data[index])
        # Call the recursive fucntion with the new slate now
        perm_helper(data, index+1, slate)
        #since the slate is mutable we need to pop the element we added
        slate.pop()
        # place the swapped element back in place
        data[pick], data[index] = data[index], data[pick]

    return


print(permutation_46(nums))

