class Solution:
    # my solution
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = sorted(nums)
        
        res = [1 if a != b else 0 for a, b in zip(nums, tmp)]
        
        for n in res:
            if n == 1:
                break
            else:
                res = res[1:]
                
        for n in res[::-1]:
            if n == 1:
                break
            else:
                res = res[:-1]
            
        return len(res)
    
    # more concise solution
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103052/Python-Sort-Solutions
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = [a == b for a, b in zip(nums, sorted(nums))]
        
        return 0 if all(res) else len(res) - res.index(0) - res[::-1].index(0)