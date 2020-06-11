
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
# such that no two queens attack each other.


# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

import time

n = 8

result = []


def nqueens_51():
    #start with 0 to make it easy to work with lists
    nqueens_helper(0, [])
    return result

def nqueens_helper(index, slate):
    # Back tracking case
    # All backtracing inside conflict resolution

    # # I have to detect the conflict between q(i-1) and earlier queen
    # last_queen = len(slate) -1  # len(slate) will be equal to the queens aready placed in the board
    # # check for coloum conflicts
    # # we do not need to perform row conflicts check as we are assming each queen is already placed in a new row
    # for past_queens in range(last_queen):
    #     if slate[past_queens] == slate[last_queen]:
    #         # Since conflict found we prune this tree
    #         return 

    #     # now we need to check that the diagonal are not in conflict
    #     # for a diagonal to be in conflict the difference in the row values and coloum values need to be equal
    #     # example Qa1 and Qd4 here 4-1 is 3 and d-a is also 3 assming a is 1 and d is 4
    #     col_diff = abs(last_queen - past_queens)
    #     row_diff = abs(slate[last_queen] - slate[past_queens])
    #     if col_diff == row_diff:
    #         return

    # Base case
    if index == n:
        result.append(slate[:])
        return
    

    # Recursion cases
    for row in range(0, n):
        # If you want to try a less optimized but still working code
        # here when n = 12 time taken 10.133749961853027
        # Queen index to be placed in any row = row which is not already taken
        if resolve_conflict(row, slate):
            slate.append(row)
            nqueens_helper(index+1, slate)
            slate.pop()
        # So lets try to optimize by eleminating the rows already selected
        # tried to optimize for row selection
        # for pick in range(row, n):
        #     # We swap index with the pick
        #     pick, index = index, pick
        #     slate.append(index)
        #     nqueens_helper(index+1, slate)
        #     slate.pop()
        #     pick, index = index, pick
    return

def resolve_conflict(row, slate):
    # Eleminate already used coloums
    for queen_col in range(len(slate)):
        if slate[queen_col] == row:
            return False
        
        col_diff = abs(len(slate) - queen_col)
        row_diff = abs(row - slate[queen_col])

        if row_diff == col_diff:
            return False
        
    return True
    

if __name__ == "__main__":
    start_time = time.time()
    # here when n = 12 time taken 10.133749961853027
    # with optimized solution when n = 12 time taken 8.952171325683594
    out = nqueens_51()
    print("time taken to solve =" + str(time.time() - start_time))
    count = 0
    # print(out[0])
    for pos in range(len(out)):
        # for j in range(len(out[pos])):
        #     print(out[pos][j], end=' ')
        # print("\n")
        count +=1
    
    print(count)
    

    # print(nqueens_51())
    # print(len(nqueens_51()))
