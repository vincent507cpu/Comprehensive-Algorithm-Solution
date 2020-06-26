class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        if not s:
            return 0
            
        dct = {}
        res, maxFreq, j = 0, 0, 0
        
        for i in range(len(s)):
            while j < len(s) and j - i - maxFreq <= k:
                dct[s[j]] = dct.get(s[j], 0) + 1
                maxFreq = max(maxFreq, dct[s[j]])
                j += 1
            
            if j - i - maxFreq > k:
                res = max(res, j - i - 1)
            else:
                res = max(res, j - i)
                
            dct[s[i]] -= 1
            maxFreq = max(dct.values())
            
        return res