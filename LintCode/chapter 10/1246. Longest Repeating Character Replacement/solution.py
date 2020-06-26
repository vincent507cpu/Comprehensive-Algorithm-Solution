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
            
        max_freq, res, dct = 0, 0, {}
        j = 0
        
        for i in range(len(s)):
            while j < len(s) and j - i - max_freq <= k:
                dct[s[j]] = dct.get(s[j], 0) + 1
                max_freq = max(max_freq, dct[s[j]])
                j += 1
                
            if j - i - max_freq > k:
                res = max(res, j - i - 1)
            else:
                res = max(res, j - i)
                
            dct[s[i]] -= 1
            max_freq = max(dct.values())
            
        return res