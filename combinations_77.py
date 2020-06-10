# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


# n means out input dataset is 1,2,3,4,....,n
# In the case of n=4 out data set is [1,2,3,4]
n = 4 
# k means that how many numbers i will pick from the n integers?
# Here k =2 means pick 2 numbers out of a data string[1,2,3,4]
k = 2
result = []

def combinations_77(n,k):
    # data = range(n)
    # print(data)
    combination_helper(n+1  ,1,[])

    return result
    
def combination_helper(length, index, slate):
    # Backtrack Case
    
    # Why are we doing the back track before even checking the base case? 
    # Why should we even bother to generate or check for a leafe case if the result is not going to be needed anyways
    # Due to this the back track case comes even before the base case
    if len(slate) == k:
        result.append(slate[:])
        return
    
    # Base case

    # Why is the base case needed??
    if index == length:
        #no op
        return

    # Recursive case
    # Ensure no repeat values
    count = 1
    for _ in range(index, length):
        if index != length:
            break
        count +=1
    # Exclude
    # exclude choice we have the same slate with index incremented thus reducing the problem size
    combination_helper(length, index+count, slate)

    # Include
    # in include case i add a value to slate and pop it out later
    for _ in range(1, count+1):
        slate.append(index)
        combination_helper(length, index+count, slate)

    for _ in range(1, count+1):
        slate.pop()

    return


print(combinations_77(4,2))