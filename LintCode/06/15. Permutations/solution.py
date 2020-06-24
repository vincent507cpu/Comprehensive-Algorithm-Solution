class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        res = []
        self.dfs(nums, [], set(), res)
        return res
        
    def dfs(self, nums, permutaion, visited, res):
        if len(permutaion) == len(nums):
            res.append(permutaion[:])
            return
            
        for num in nums:
            if num in visited:
                continue
            
            permutaion.append(num)
            visited.add(num)
            self.dfs(nums, permutaion, visited, res)
            permutaion.pop()
            visited.remove(num)