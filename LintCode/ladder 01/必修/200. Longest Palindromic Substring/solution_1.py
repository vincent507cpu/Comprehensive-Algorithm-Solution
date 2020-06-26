# DP

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        res = [[False] * n for _ in range(n)]
        
        for i in range(n):
            res[i][i] = True
            if i > 0:
                res[i][i-1] = True
                
        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                res[i][j] = res[i+1][j-1] and s[i] == s[j]
                if res[i][j] and length > longest:
                    longest = length
                    start = i
                    
        return s[start:start+longest]