# https://leetcode.com/problems/subsets-ii/
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


nums = [1,2,2]
result = []

def subset2_90(nums):
    nums.sort()
    subset2_helper(nums, 0, [])

    return result

def subset2_helper(data, index, slate):
    #base case
    if index == len(data):
        result.append(slate[:])
        return
    
    # else:
    # For the recursive case
    #check how many copies of the data[i] are present
    count = 0
    for i in range(index, len(data)):
        if data[i] != data[index]:
            break
        count +=1
    
    # there are two choices to exclude and include 
    # Exclude case
    # in the exlude case we make the index jump over all the duplicates in the sorted array
    subset2_helper(data, index + count, slate)

    # Include case 
    # here we need to take care of all the duplicates captured in count
    
    for _ in range(1,count+1):  #Count +1 is essential otherwise we dont enter for loop for single element
        slate.append(data[index])
        # important that the index is still incrementd by index + count as i wanted all the branches to 
        # get the non index values only in the branch. we manually add the repeated values in the slate
        subset2_helper(data, index + count, slate)

    for _ in range(1, count+1): # Count+1 is essential otherwise the non=repeated element does not get poped out
        slate.pop()

    return


print(subset2_90(nums)) 
    