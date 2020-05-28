class Solution:
    # my solution
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        tmp = 0
        
        for n in A:
            tmp = tmp * 2 + n
            res.append(tmp % 5 == 0)
            
        return res
    
    # faster solution
    # https://leetcode.com/problems/binary-prefix-divisible-by-5/discuss/265509/Python-Calculate-Prefix-Mod
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        B = A[:]
        
        for i in range(1, len(B)):
            B[i] += B[i-1] * 2 % 5
            
        return [b % 5 == 0 for b in B]