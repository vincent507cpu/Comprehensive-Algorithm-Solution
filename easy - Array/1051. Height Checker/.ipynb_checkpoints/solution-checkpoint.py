class Solution:
    # my solution
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights)
        res = 0
        
        for i, j in zip(ordered, heights):
            if i != j:
                res += 1
                
        return res