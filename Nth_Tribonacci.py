# https://leetcode.com/problems/n-th-tribonacci-number/
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:
# Input: n = 25
# Output: 1389537
# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
# class Solution:
# def tribonacci(self, n):

# def helper(self, index, tn, tn1, tn2):
class Solution:

    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        t0 = 0
        t1 = 1
        t2 = 1
        
        for _ in range(n-2):
            t0,t1,t2 = t1,t2,t0+t1+t2
        
        return t2
    
    # Works but exceeds memory
    # Class variables
    # result = 0
    # def __int__(self, n):
    #     # self.result = []
    #     self.n = n

    # # result = []

    # def helper(self, index, tn, tn1, tn2,n):
    #     # Base Case
    #     if index == n +1:
    #         return self.result
        
    #     self.result = tn + tn1 + tn2
        
    #     self.helper(index+1,tn1,tn2,self.result,n)

    #     return self.result

    # def tribonacci(self,n):

    #     # self.result = 0
    #     t0 = 0
    #     t1 = 1
    #     t2 = 1

    #     self.helper(3,t0,t1,t2,n)
    #     return self.result


if __name__ == "__main__":
    obj = Solution()
    print(obj.tribonacci(4))
    # print(tribonacci(4))