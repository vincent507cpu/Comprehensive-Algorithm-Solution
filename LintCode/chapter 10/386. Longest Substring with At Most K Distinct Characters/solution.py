class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        dct, res, unique = {}, 0, 0
        i, j = 0, 0
        
        while j < len(s):
            # while unique <= k:
            if s[j] not in dct or dct[s[j]] == 0:
                dct[s[j]] = 1
                unique += 1
            else:
                dct[s[j]] += 1
            j += 1

            while unique > k:
                dct[s[i]] -= 1
                if dct[s[i]] == 0:
                    unique -= 1
                i += 1

            res = max(res, j - i)
            
        return res