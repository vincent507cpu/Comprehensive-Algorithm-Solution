# three solutions, some are consulted from
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/543154/3-solutions-or-Easy-to-Understand-or-Faster-or-Python

class Solution:
    # No. 1: use set
    def repeatedNTimes(self, A: List[int]) -> int:
        res = set()
        
        for n in A:
            if n in res:
                return n
            else:
                res.add(n)
                
    # No. 2: calculate
    def repeatedNTimes(self, A: List[int]) -> int:
        res = set(A)
        
        repeated_val = sum(A) - sum(res)
        repeated_time = len(A) - len(res)
        
        return repeated_val // repeated_time
    
    # No.3: use constant space
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                return A[i]