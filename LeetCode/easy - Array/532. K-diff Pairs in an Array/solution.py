class Solution:
    # my solution
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        dct = {}
        
        for n in nums:
            dct[n] = dct.get(n, 0) + 1
        if k == 0:
            return sum([1 for val in dct.values() if val > 1])
        
        res = 0
        for key in dct.keys():
            if key+k in dct.keys():
                res += 1
                
        return res