class Solution:
    # my solution
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(0, len(nums), 2):
            res += nums[i] * [nums[i+1]]
            
        return res
    
    # more concise solution
    # https://leetcode.com/problems/decompress-run-length-encoded-list/discuss/477055/Python-1-Line-with-Intuition
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [x for a, b in zip(nums[0::2], nums[1::2]) for x in [b] * a]