class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
            
        n = len(s)
        
        dp = [0, 0, 0]
        dp[0] = 1
        dp[1] = self.is_valid(s[0])
        
        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] * self.is_valid(s[i - 1:i]) + \
                        dp[(i - 2) % 3] * self.is_valid(s[i - 2:i])
                        
        return dp[n % 3]
    
    def is_valid(self, digits):
        num = int(digits)
        if len(digits) == 1 and 0 < num <= 9:
            return 1
        if len(digits) == 2 and 10 <= num <= 26:
            return 1
            
        return 0