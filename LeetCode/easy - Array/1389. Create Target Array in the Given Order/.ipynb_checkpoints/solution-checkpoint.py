class Solution:
    # my solution, using `insert`
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
            
        return res
    
    # without using `insert`
    # https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/553334/Python-Using-insert()-and-without-insert()
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            res = res[:index[i]] + [nums[i]] + res[index[i]:]
            
        return res
    
    # https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/564981/Python-Straightforward-Solution-with-3-Lines
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        
        [res.insert(idx, n) for idx, n in zip(index, nums)]
        
        return res