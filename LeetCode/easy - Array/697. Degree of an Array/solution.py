class Solution:
    # my solution
    def findShortestSubArray(self, nums: List[int]) -> int:
        dct = {}
        
        for i, n in enumerate(nums):
            dct[n] = dct.get(n, []) + [i]
            
        
        dct = {key:val for key, val in dct.items() if len(val) == max([len(val) for val in dct.values()])}
        
        res = float('inf')
        
        for val in dct.values():
            res = min(res, max(val)-min(val)+1)
            
        return res
    
    # better solution
    # https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC%2B%2BPython-One-Pass-Solution
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count, res, degree = {}, {}, 0, 0
        
        for i, a in enumerate(A):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
                
        return res