# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-639-3332-34-236
# Generate All Possible Expressions That Evaluate To The Given Target Value

# Given a string s that consists of digits (“0”..”9”) and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.
# When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: “join” or “*” or “+”. For example, by inserting different operators between the two characters of string “12” we can get either 12 (1 joined with 2) or 2 (1*2) or 3 (1+2).
# Other operators such as “-” or “÷” are NOT supported.
# Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.
# Precedence of the operators is conventional: “join” has the highest precedence, “*” – medium and “+” has the lowest precedence. For example, 1+2*34=(1+(2*(34)))=1+68=69.
# You have to return ALL expressions that can be built from string s and evaluate to the target.
# Example One
# Input:
# s="222", target=24.
# Output:
# ["22+2", "2+22"] and ["2+22", "22+2"] are both correct outputs.
# 22+2=24: we inserted the “join” operator between the first two characters and the “+” operator between the last two characters of s.
# 2+22=24: we inserted the “+” operator between the first two characters and the “join” operator between the last two characters of s.

# Example Two
# Input: s="1234", target=11.
# Output: ["1+2*3+4"]

# Example Three
# Input:
# s="99", target=1.
# Output:
# []

# Failing on the following inputs
# 1: Failling because 0 is at the start??
# input: 0123456789012, target: 123456789012
# YOUR OUTPUT 15 chars : 0+123456789012
# EXPECTED OUTPUT 63 chars
# 2 different expressions possible.
# 0+123456789012
# 0123456789012
# 
# 2: Failing due to repeat incharacters?
# input: 9909059799853, target:764
# YOUR OUTPUT 691 chars
# 9909*0*5+9*7+9*9*8+53
# 990*9*0*5+9*7+9*9*8+53
# 99+0+90+5*9+7+99+8*53
# ...

# EXPECTED OUTPUT 1116 chars
# 46 different expressions possible.
# 9+9+0+9*0+59+7*9*9+8*5*3
# 9+9+0*9+0+59+7*9*9+8*5*3
# 9+9+0*9*0+59+7*9*9+8*5*3
# ...
# 3
# input: 40404040, target: 0
# 311 different expressions possible., my output is much lesser

s = ['1','2','3','4']
target = 11

def generate_all_expressions(s, target):
    
    #creare a results list
    results = []
    # Create the helper function
    generate_helper(0, 0, 0, 0, [], results)
    
    return results
    

def generate_helper(prev_op, current_op, index, value, slate, results):
    #backtracking case
    # if results[0] == target:
    #     results.append(slate[1:])
    #     return
    
    # elif results[0] < target:
    #     pass
    
    #base case
    if index == len(s):
        # check the values here
        if value == target and current_op == 0:
            results.append("".join(slate[1:]))
        return
    
    #recursive case
    # extending the current operand by 1 digit
    current_op = current_op * 10 + int(s[index])
    #building the string here??
    slate_op = str(current_op)

    # exite any cases where current op become 0
    if current_op > 0:
        #call the left side by incrementing the index
        generate_helper(prev_op, current_op, index+1, value, slate, results)
        
    # call the right side of the tree
    # MULTIPLICATION
    # since we add a new vairable we need to pop it out
    slate.append('+')
    slate.append(slate_op)
    generate_helper(current_op, 0, index+1, value + current_op, slate, results)
    #pop out the 2 added elements
    slate.pop()
    slate.pop()

    if slate:
        #check for the addition case also here
        slate.append('*')
        slate.append(slate_op)
        generate_helper(current_op * prev_op, 0, index+1, value - prev_op + (current_op*prev_op), slate, results)
        #pop out the 2 added elements
        slate.pop()
        slate.pop()
    
print(generate_all_expressions(s, target))