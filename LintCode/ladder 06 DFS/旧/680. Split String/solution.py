class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, split, res):
        if s == '':
            res.append(split[:])
            return
        
        for i in range(2):
            if i + 1 <= len(s):
                split.append(s[:i + 1])
                self.dfs(s[i + 1:], split, res)
                split.pop()