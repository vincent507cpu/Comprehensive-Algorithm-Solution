class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        res = []
        self.dfs(n, k, 1, [], res)
        return res
        
    def dfs(self, n, k, start_index, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(start_index, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path, res)
            path.pop()