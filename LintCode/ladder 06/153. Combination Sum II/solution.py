# https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        if not num:
            return []
            
        if not target:
            return [[]]
            
        num.sort()
        res = []
        self.dfs(num, target, [], 0, res)
        return res
        
    def dfs(self, num, target, combination, start, res):
        if target == 0:
            res.append(combination)
            return
        
        for i in range(start, len(num)):
            if i > start and num[i] == num[i - 1]:
                continue
            
            if num[i] > target:
                break
            
            self.dfs(num, target - num[i], combination + [num[i]], i + 1, res)