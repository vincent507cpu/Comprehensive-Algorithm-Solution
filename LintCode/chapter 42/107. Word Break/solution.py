# DP
# DFS solution see 

class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        max_length = max([len(w) for w in wordSet]) if wordSet else 0
        
        for i in range(1, n + 1):
            for j in range(1, max_length + 1):
                if i < j:
                    break
                if not dp[i - j]:
                    continue
                
                word = s[i - j:i]
                if word in wordSet:
                    dp[i] = True
                    break
                
        return dp[n]