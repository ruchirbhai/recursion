# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
# Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
import time

S = ["a1b2", "3z4", "12345","abcd"]
result = []

def letter_case_perm(data):
    # Create the result bag where you get the final answer
    
    lcp_helper(data, 0, []) # for mutabable array our empty slate will be a empty list
    return result


def lcp_helper(data, index, slate):
    #base case : Leaf worker
    if index == len(data):
        result.append("".join(slate)) # add a snapshot of the mutable string
        return
    
    # If we are an internal node its the recursive case
    if data[index].isdigit(): #if it is a digit one choice
        #append the new index to the mutable slate
        slate.append(data[index])
        # Call the helper with the new slate
        lcp_helper(data, index+1, slate)
        # Remove the added last element before returning back
        slate.pop()
    
    else: # if data[i] is alpha we have 2 choices
        #choice 1 lower case
        #append the new index to the mutable slate
        slate.append(data[index].lower())
        lcp_helper(data, index+1,slate)
        # Remove the added last element before returning back
        slate.pop()

        #choice 2 upper case
        slate.append(data[index].upper())
        lcp_helper(data, index+1,slate)
        # Remove the added last element before returning back
        slate.pop()    
    return

if __name__ == "__main__":
    #call the test dataset
    for i in range(len(S)):
        start_time = time.time()
        bag =letter_case_perm(S[i])
        print("letter case permutation" + str(i+1) + " = "+ str(time.time() - start_time))
        print(bag)