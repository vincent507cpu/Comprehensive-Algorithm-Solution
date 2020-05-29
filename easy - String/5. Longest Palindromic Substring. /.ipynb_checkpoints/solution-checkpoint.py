class Solution:
    # two pointers
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ''
        
        res = (0, 0)
        for i in range(len(s)):
            res = max(res, self.isPalindrom(s, i, i))
            res = max(res, self.isPalindrom(s, i, i + 1))
            
        return s[res[1]:res[0]+res[1]]
        
    def isPalindrom(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1, l + 1
    
    # dynamic progrmming
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ''
        
        n = len(s)
        is_palindrom = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrom[i][i] = True
        for i in range(1, n):
            is_palindrom[i][i-1] = True
            
        start, long = 0, 1
        for length in range(2, n + 1):
            for i inrange(n - length + 1):
                j = i + length - 1
                is_palindrom[i][j] = is_palindrom[i + 1][j - 1] and s[i] == s[j]
                if is_palindrom[i][j] and length > long:
                    long = length
                    start = i
                    
        return s[start:start + length]