class Solution:
    # my solution
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not List:
            return []
        
        tmp = []
        for row in nums:
            tmp += row
        # this three lines can be compressed into:
        # tmp = sum(nums, [])
        
        if len(tmp) != r * c:
            return nums
        
        return [tmp[n:n+c] for n in range(0, len(tmp), c)]
    
    