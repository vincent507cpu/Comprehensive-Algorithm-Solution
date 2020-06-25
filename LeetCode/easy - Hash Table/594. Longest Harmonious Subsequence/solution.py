# best solution
# https://leetcode.com/problems/longest-harmonious-subsequence/discuss/103518/Python-119ms-beats-99-submissions-with-explanation

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dct = {}
        
        for n in nums:
            dct[n] = dct.get(n, 0) + 1
            
        res = 0
        
        for n in dct:
            if dct.get(n+1):
                res = max(res, dct[n] + dct[n+1])
            
        return res