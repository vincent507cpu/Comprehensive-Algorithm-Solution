class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
        
    def dfs(self, candidates, remaining, start, combination, result):
        if not remaining:
            result.append(combination[:])
            return
        
        for i in range(start, len(candidates)):
            if remaining < 0:
                return
            
            remaining -= candidates[i]
            combination.append(candidates[i])
            self.dfs(candidates, remaining, i, combination, result)
            remaining += candidates[i]
            combination.pop()