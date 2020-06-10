# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

nums = [1,1,2,]
result = []

def permutation_47(nums):
    # call the helper function
    perm2_helper(nums, 0)
    return result

# Helper function code
def perm2_helper(data, index):
    # Base case
    if index == len(data):
        result.append(data[:])
    # recursion part
    else:
        # Create a hash table to ensure only unique branches created at each node level
        hmap = {}

        for pick in range(index,len(data)):
            if data[pick] not in hmap:  #to ensure that no duplicate branches are created
                hmap[data[pick]] = 1
                #swap the pick and index values so we do not ignore the values on the left of the pick
                data[pick],data[index] = data[index], data[pick]
                # Add the pick to the slate and continue making the tree
                # slate.append(data[pick])
                perm2_helper(data, index+1)
                # slate.pop() # we need to remove the element we added to slate before passing it on
                #swap the data element back in place before completing one branch
                data[pick],data[index] = data[index], data[pick]
        return
    

print(permutation_47(nums))
