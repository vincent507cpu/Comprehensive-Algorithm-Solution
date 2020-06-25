class Solution:
    # my initail solution, O(nlogn) time
    def dominantIndex(self, nums: List[int]) -> int:
        big, flag = max(nums), True
        idx = nums.index(big)
        
        for i, n in enumerate(nums):
            if big != n and big < n * 2:
                return -1
            
        return idx
    
    # better solution, O(n) time
    def dominantIndex(self, nums: List[int]) -> int:
        big = small = -float('inf')
        idx = 0
        
        for i, n in enumerate(nums):
            if n > big:
                small = big
                idx = i
                big = n
            elif n > small:
                small = n
                
        if big >= small * 2:
            return idx
        else:
            return -1