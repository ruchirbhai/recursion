# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all 
# combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

n = 3

result = []

def gen_parentheses_22(n):
    # Call helper function

    gen_parentheses_helper(n,n,[])

    return result

def gen_parentheses_helper(num_left, num_right, slate):
    # back track case
    # When num_left > num_right it means that well formed array 
    # cannot happen example "(()))" num_left = n-2 i.e 1 
    # and num_right = 0
    if num_right < num_left:
        # in this case we will never have well formed parenthesis
        return
    # Base case
    if num_left == 0 and num_right == 0:
        result.append("".join(slate))
        return
    
    # recursive case
    # include '('
    if num_left > 0:
        slate.append('(')
        gen_parentheses_helper(num_left -1, num_right, slate)
        slate.pop()
    
    # include ')'
    if num_right > 0:
        slate.append(')')
        gen_parentheses_helper(num_left, num_right-1,slate)
        slate.pop()
    
    return


print(gen_parentheses_22(n))

